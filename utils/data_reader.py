import csv

def get_product_list():
    with open("data/products.csv") as f:
        return [row["product_name"] for row in csv.DictReader(f)]
