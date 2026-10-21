fruits = {}

for i in range(6):
    name = input("Enter fruit name: ")
    buying = float(input("Enter buying price: "))
    selling = float(input("Enter selling price: "))
    fruits[name] = (buying, selling)

profit = []
loss = []
no_profit_no_loss = []

for name, prices in fruits.items():
    buying, selling = prices
    if selling > buying:
        profit.append(name)
    elif buying > selling:
        loss.append(name)
    else:
        no_profit_no_loss.append(name)

print("Profit fruits:", profit)
print("Loss fruits:", loss)
print("No profit, no loss:", no_profit_no_loss)
