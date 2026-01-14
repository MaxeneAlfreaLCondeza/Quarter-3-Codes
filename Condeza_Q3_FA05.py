names = ["Me", "Lia", "Jake"]
steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Calculate total steps per day
day_totals = []
for j in range(5):
    total = 0
    for i in range(3):
        total += steps[i][j]
    day_totals.append(total)
    print(days[j], "total steps:", total)

# Find the most active day
most_active = day_totals[0]
most_active_day = days[0]
for j in range(1, 5):
    if day_totals[j] > most_active:
        most_active = day_totals[j]
        most_active_day = days[j]

print("Most active day:", most_active_day, "with", most_active, "steps")
