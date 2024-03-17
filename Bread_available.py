# Check if there is bread in bread bin
bread_bin = False
if bread_bin:
    print("There is bread, let's make a sandwich")
else:
    print("There is no bread, we have to buy bread")

# If there is no bread, check wallet for 20 to buy bread
wallet = 100
if wallet > 20:
    print("We have more than enough cash to buy bread")
else:
    print("We don't seem to have enough cash on hand, let's order food online.")

# Check which shop has Sasko or Albany at the lowest price and buy it
shop1_bread_stock = {
    "nesta": 15,
    "original": 10,
    "blueribbon": 18,
}

shop2_bread_stock = {
    "albany": 25,
    "nesta": 18,
    "Sasko": 16,
    "original": 21,
    "blue ribbon": 22,
}

# Find the lowest price for "albany" or "Sasko" bread
lowest_price = min(shop1_bread_stock.get("albany", float("inf")), shop1_bread_stock.get("Sasko", float("inf")),
                   shop2_bread_stock.get("albany", float("inf")), shop2_bread_stock.get("Sasko", float("inf")))

if lowest_price == float("inf"):
    print("No shop has 'albany' or 'Sasko' bread")
else:
    for shop, price in shop1_bread_stock.items():
        if price == lowest_price and ("albany" in shop or "Sasko" in shop):
            print(f"{shop.capitalize()} has the lowest price for 'albany' or 'Sasko' bread, so we're buying from {shop}.")
            break
    else:
        for shop, price in shop2_bread_stock.items():
            if price == lowest_price and ("albany" in shop or "Sasko" in shop):
                print(f"{shop.capitalize()} has the lowest price for 'albany' or 'Sasko' bread, so we're buying from {shop}.")
                break
        else:
            print("There is no 'albany' or 'Sasko' bread at the lowest price in any shop.")
