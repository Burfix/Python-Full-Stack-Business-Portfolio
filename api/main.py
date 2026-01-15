from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import csv
import io

app = FastAPI(title="Supplier Price API", version="0.2.0")


class CSVPayload(BaseModel):
    csv_text: str


@app.get("/")
def health_check():
    return {"status": "API is running"}


def compute_insights(csv_text: str) -> dict:
    f = io.StringIO(csv_text)
    reader = csv.DictReader(f)

    required = {"item", "supplier", "price"}
    if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
        raise KeyError(f"CSV must include headers: {sorted(required)}")

    min_per_item = {}
    max_per_item = {}

    for row in reader:
        item_raw = row["item"]
        supplier = row["supplier"].strip()
        price = float(row["price"])

        # Normalise item key to prevent duplicates like "Olive Oil" vs "olive oil"
        item_key = item_raw.strip().lower()

        if item_key not in min_per_item or price < min_per_item[item_key]["price"]:
            min_per_item[item_key] = {"supplier": supplier, "price": price}

        if item_key not in max_per_item or price > max_per_item[item_key]["price"]:
            max_per_item[item_key] = {"supplier": supplier, "price": price}

    # Totals + savings
    total_min = round(sum(v["price"] for v in min_per_item.values()), 2)
    total_max = round(sum(v["price"] for v in max_per_item.values()), 2)
    total_savings = round(total_max - total_min, 2)

    savings_by_item = {}
    supplier_wins = {}
    supplier_spend = {}

    for item_key, cheap in min_per_item.items():
        expensive = max_per_item[item_key]
        savings = round(expensive["price"] - cheap["price"], 2)

        savings_by_item[item_key] = {
            "cheapest_supplier": cheap["supplier"],
            "cheapest_price": round(cheap["price"], 2),
            "most_expensive_supplier": expensive["supplier"],
            "most_expensive_price": round(expensive["price"], 2),
            "savings": savings,
        }

        s = cheap["supplier"]
        supplier_wins[s] = supplier_wins.get(s, 0) + 1
        supplier_spend[s] = round(supplier_spend.get(s, 0.0) + cheap["price"], 2)

    return {
        "cheapest": min_per_item,
        "total_cheapest": total_min,
        "total_most_expensive": total_max,
        "total_savings": total_savings,
        "savings_by_item": savings_by_item,
        "supplier_scoreboard": {"wins": supplier_wins, "spend": supplier_spend},
    }


@app.post("/cheapest")
def cheapest(payload: CSVPayload):
    try:
        return compute_insights(payload.csv_text)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError:
        raise HTTPException(status_code=400, detail="Price must be numeric")


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        content = await file.read()
        csv_text = content.decode("utf-8")
        return compute_insights(csv_text)
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be a UTF-8 CSV")
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError:
        raise HTTPException(status_code=400, detail="Price must be numeric")
