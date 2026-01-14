 # Prices of items (Rice, Milk, Eggs) from different grocery stores
prices = [
    [55, 90, 180], # grocery store 1
    [58, 85, 175], # grocery store 2 
    [53, 92, 185]  # grocery store 3 
]

# Access a price
print(prices[1][0])

# Total per store
for store in prices:
    print(sum(store))    

 # Highest price
print(max(max(store) for store in prices)) 
