# Q5 - DSDV proactive routing-table simulation
cases=[(10,2),(25,4),(50,6)]
print("Q5 - DSDV PROACTIVE ROUTING")
print("Nodes | Update rounds | Table entries | Control updates | Route availability")
for nodes,rounds in cases:
    entries=nodes*(nodes-1)
    updates=nodes*rounds
    print(f"{nodes} | {rounds} | {entries} | {updates} | 100% (stable topology)")
print("Sequence numbers identify fresh routes and help prevent routing loops.")
print("Trade-off: routes are ready when needed, but periodic updates consume bandwidth.")
