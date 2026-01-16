import csv

def load_invoice_rows(csv_path: str) -> list[dict]:
    """Load invoice rows from a CSV file into a list of dictionaries."""
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def find_cheapest_per_item(rows: list[dict]) -> dict:
    """
    Business logic:
    For each item, find the supplier offering the lowest price.
    Returns: { item_name: {"supplier": str, "price": float} }
    """
    cheapest: dict = {}

    for row in rows:
        item = row["item"].strip()
        supplier = row["supplier"].strip()
        price = float(row["price"])

        if item not in cheapest or price < cheapest[item]["price"]:
            cheapest[item] = {"supplier": supplier, "price": price}

    return cheapest


def print_summary(cheapest: dict) -> None:
    print("\nCheapest supplier per item:")

    total = 0.0
    for item in sorted(cheapest.keys()):
        data = cheapest[item]
        total += data["price"]
        print(f"- {item}: {data['supplier']} at R{data['price']:.2f}")

    print(f"\nTotal (1 of each item): R{total:.2f}")



def main() -> None:
    print("=== Invoice Parser v2 ===")
    csv_path = input("Enter invoice CSV filename: ").strip()

    try:
        rows = load_invoice_rows(csv_path)
        cheapest = find_cheapest_per_item(rows)
        print_summary(cheapest)
    except FileNotFoundError:
        print("File not found. Check the filename/path.")
    except KeyError as e:
        print(f"Missing expected column in CSV: {e}")
    except ValueError:
        print("Price must be a number. Check the 'price' column values.")


if __name__ == "__main__":
    main()