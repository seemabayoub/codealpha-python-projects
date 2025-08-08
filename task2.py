equities = {
    "BLU": 220,
    "GRN": 280,
    "YLO": 140,
    "RED": 110
}
overall_value = 0
num_equities = int(input("Enter count of equities: "))
for _ in range(num_equities):
    equity = input("Enter equity code: ").upper()
    volume = int(input("Enter volume: "))
    if equity in equities:
        rate = equities[equity]
        cost = rate * volume
        overall_value += cost
    else:
        print("Equity not listed")
print(f"Total value: {overall_value}")
with open("investments.txt", "w") as doc:
    doc.write(f"Total value: {overall_value}")
print("Data saved")
