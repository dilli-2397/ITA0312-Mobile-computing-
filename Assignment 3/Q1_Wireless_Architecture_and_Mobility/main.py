signals = [-55, -62, -71, -79, -83, -60, -68, -78, -82, -58]
threshold = -75
handoffs = 0
connected = True
print("Q1 - WIRELESS MOBILITY AND HANDOFF")
print("Step | Signal dBm | Network state")
for i, signal in enumerate(signals, 1):
    if signal < threshold:
        handoffs += 1
        state = "Handoff triggered"
    else:
        state = "Connected"
    print(f"{i:>4} | {signal:>10} | {state}")
print(f"Total handoff events: {handoffs}")
print("Model: a handoff is triggered whenever signal falls below -75 dBm.")