tests = [(10, "Low", 98.0, 35, 18),
         (25, "Medium", 94.0, 62, 120),
         (50, "High", 86.0, 115, 490)]
print("Q7 - MOBILE EMERGENCY NETWORK VALIDATION")
print("Nodes | Mobility | Packet delivery % | Delay ms | Control messages")
for nodes, mobility, pdr, delay, overhead in tests:
    print(f"{nodes:>5} | {mobility:<8} | {pdr:>17.1f} | {delay:>8} | {overhead:>16}")
print("Selected architecture: wireless ad hoc network with gateway support.")
print("Selected routing: AODV for on-demand route discovery and repair.")
print("Failure plan: use alternate route; buffer messages during total disconnection.")
print("Test values are illustrative scenarios, not measured device/network results.")