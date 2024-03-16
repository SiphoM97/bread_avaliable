bread_stock = ["albany", "nesta", "sasko", "original", "blueribbon"]

bread_stock.remove("albany")
bread_stock.remove("sasko")

# Check if 'albany' and 'sasko' are available in the list
if "albany" in bread_stock or "sasko" in bread_stock:
    print("Buy bread")
else:
    print("Coming back with the money")
