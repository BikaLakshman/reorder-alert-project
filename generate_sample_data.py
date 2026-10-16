"""Creates a made-up inventory file (inventory.csv) so the project can run without real data."""
import random
import pandas as pd

random.seed(42)  # same data every run

categories = {
    "Grocery": ["Cereal", "Pasta", "Canned Soup", "Granola Bars", "Coffee", "Peanut Butter"],
    "Household": ["Paper Towels", "Laundry Detergent", "Trash Bags", "Dish Soap", "Sponges"],
    "Electronics": ["USB Cable", "Earbuds", "Phone Charger", "HDMI Cable", "Batteries"],
    "Apparel": ["Socks", "T-Shirt", "Hoodie", "Baseball Cap", "Gloves"],
    "Toys": ["Board Game", "Puzzle", "Action Figure", "Plush Toy", "Card Game"],
}

rows, item_id = [], 1000
for category, items in categories.items():
    for name in items:
        weekly_sales = random.randint(10, 120)
        # stock ranges from nearly empty to well stocked
        stock = int(weekly_sales * random.uniform(0.1, 6))
        rows.append({
            "item_id": item_id,
            "item_name": name,
            "category": category,
            "stock_on_hand": stock,
            "avg_weekly_sales": weekly_sales,
            "lead_time_days": random.choice([3, 5, 7, 10, 14]),  # days for a restock to arrive
        })
        item_id += 1

rows[3]["stock_on_hand"] = 0  # one item fully out of stock for the demo
pd.DataFrame(rows).to_csv("inventory.csv", index=False)
print(f"Created inventory.csv with {len(rows)} items")
