routes = {
    "A": ("A", 0, 10),
    "B": ("B", 1, 12),
    "C": ("C", 1, 14),
    "D": ("B", 2, 16)
}
print("Q5 - DSDV ROUTING TABLE")
print("Destination | Next hop | Hop count | Sequence")
for dest, row in routes.items():
    print(f"{dest:^11} | {row[0]:^8} | {row[1]:^9} | {row[2]}")
print("Event: link B-D fails; a fresh route advertisement arrives via C.")
routes["D"] = ("C", 2, 18)
print("Updated route to D:", routes["D"])
print("DSDV uses destination sequence numbers to prefer fresh routes.")
print("A periodic update maintains routes even before data is requested.")