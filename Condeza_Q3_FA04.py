names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = [sum(s) for s in steps]

for i in range(3):
    print(names[i], "total steps:", totals[i])

highest = totals[0]
person = names[0]
for i in range(1, 3):
    if totals[i] > highest:
        highest = totals[i]
