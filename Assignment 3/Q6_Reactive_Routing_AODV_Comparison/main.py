tests = [(10, 2), (25, 5), (50, 10)]
print("Q6 - AODV AND DSDV CONTROL-OVERHEAD MODEL")
print("Nodes | AODV on-demand messages | DSDV periodic messages")
for nodes, active_flows in tests:
    aodv = active_flows * (nodes - 1)
    dsdv = nodes * (nodes - 1)
    print(f"{nodes:>5} | {aodv:>23} | {dsdv:>22}")
print("AODV discovers routes when traffic needs them.")
print("DSDV exchanges routing information periodically.")
print("Selection: AODV is preferred for dynamic, intermittent emergency traffic.")
print("Counts are simplified illustrative message units, not protocol packet traces.")