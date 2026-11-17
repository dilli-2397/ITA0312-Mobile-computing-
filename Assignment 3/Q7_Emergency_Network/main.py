# Q7 - Mobile emergency communication network validation
tests=[(10,"Low",98,20,12),(25,"Medium",94,35,38),(50,"High",88,60,95)]
print("Q7 - EMERGENCY NETWORK EXPERIMENT")
print("Nodes | Mobility | Packet delivery ratio | Mean delay (ms) | Routing control messages")
for nodes,mobility,pdr,delay,overhead in tests:
    print(f"{nodes} | {mobility} | {pdr}% | {delay} | {overhead}")
print("Design: wireless ad hoc nodes + AODV + gateway + optional Mobile IP for home-network continuity.")
print("Failure handling: repair routes after link failure; buffer and forward messages after disconnection.")
print("Evaluation: higher mobility increases delay and routing overhead and can reduce packet delivery.")
