import csv

print("=== Invoice Parser v1 ===")

filename = input("Enter invoice CSV filename: ")

try:
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        cheapest = {}

        for row in reader:
            item = row["item"]
            supplier = row["supplier"]
            price = float(row["price"])

            if item not in cheapest or price < cheapest[item]["price"]:
                cheapest[item] = {
                    "supplier": supplier,
                    "price": price
                }

    print("\nCheapest supplier per item:")
    for item, data in cheapest.items():
        print(f"{item}: {data['supplier']} at R{data['price']:.2f}")

except FileNotFoundError:
    print("File not found. Check the filename.")

  