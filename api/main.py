from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import csv
import io

app = FastAPI(title="Supplier Price API", version="0.1.0")


class CSVPayload(BaseModel):
    csv_text: str


@app.get("/")
def health_check():
    return {"status": "API is running"}


def compute_cheapest(csv_text: str) -> dict:
    f = io.StringIO(csv_text)
    reader = csv.DictReader(f)

    required = {"item", "supplier", "price"}
    if reader.fieldnames is None or not required.issubset(set(reader.fieldnames)):
        raise KeyError(f"CSV must include headers: {sorted(required)}")

    cheapest = {}
    for row in reader:
        item = row["item"].strip()
        supplier = row["supplier"].strip()
        price = float(row["price"])

        if item not in cheapest or price < cheapest[item]["price"]:
            cheapest[item] = {"supplier": supplier, "price": price}

    total = round(sum(v["price"] for v in cheapest.values()), 2)
    return {"cheapest": cheapest, "total": total}


@app.post("/cheapest")
def cheapest(payload: CSVPayload):
    try:
        return compute_cheapest(payload.csv_text)
    except KeyError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError:
        raise HTTPException(status_code=400, detail="Price must be numeric")
