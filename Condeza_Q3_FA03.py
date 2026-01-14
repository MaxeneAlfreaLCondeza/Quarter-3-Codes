prices = [
    [55, 90, 180],
    [58, 85, 175],
    [53, 92, 185]
]

for i in range(len(prices)):
    print("Store", i+1, "prices:", prices[i])
    print("  Total:", sum(prices[i]))
    print("  Average:", round(sum(prices[i])/len(prices[i]), 2))

print("Highest price:", max(max(prices[i]) for i in range(len(prices))))
print("Lowest price:", min(min(prices[i]) for i in range(len(prices))))
