# Q6 - AODV and DSDV comparison under changing mobility
cases=[("Low",10,10,2),("Medium",25,25,5),("High",50,50,10)]
print("Q6 - AODV VS DSDV ROUTING COMPARISON")
print("Mobility | Nodes | DSDV periodic updates | AODV route requests | DSDV setup delay | AODV setup delay")
for level,nodes,dsdv_updates,aodv_requests in cases:
    dsdv_delay=5
    aodv_delay=15 if level=="Low" else 25 if level=="Medium" else 40
    print(f"{level} | {nodes} | {dsdv_updates} | {aodv_requests} | {dsdv_delay} ms | {aodv_delay} ms")
print("DSDV keeps routes ready but sends periodic updates.")
print("AODV discovers routes on demand, reducing idle updates but adding discovery delay.")
print("For frequent topology changes, AODV is generally preferred in this model.")
