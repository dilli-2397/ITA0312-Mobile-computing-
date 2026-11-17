# Q1 - Wireless network mobility simulation
scenarios=[("Low",1,1),("Medium",3,2),("High",6,3)]
packets=100
print("Q1 - WIRELESS MOBILITY AND HANDOFF")
print("Mobility | Handoffs | Packets sent | Packets lost | Delivered | Delivery ratio")
for name,handoffs,loss_each in scenarios:
    lost=min(packets,handoffs*loss_each)
    delivered=packets-lost
    print(f"{name} | {handoffs} | {packets} | {lost} | {delivered} | {delivered/packets*100:.1f}%")
print("Model assumption: each handoff causes a short interruption and a fixed packet loss.")
