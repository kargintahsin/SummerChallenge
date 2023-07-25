# Profit Meter

cost=int(input("Enter cost: "))
price=int(input("Enter price"))

if cost>price:
    print("You can't profit")
else:
    piece=int(1+(cost/(price-cost)))
    print("How many products should you sell to make a profit? ",piece)