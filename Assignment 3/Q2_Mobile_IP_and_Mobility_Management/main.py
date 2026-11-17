events = [
    "Mobile Node enters foreign network",
    "Foreign Agent provides Care-of Address",
    "Mobile Node sends registration request",
    "Home Agent authenticates request",
    "Home Agent updates binding: Home IP -> Care-of Address",
    "Registration reply reaches Mobile Node",
    "Correspondent packet reaches Home Agent",
    "Home Agent tunnels packet to Care-of Address",
    "Foreign Agent delivers packet to Mobile Node"
]
packet_bytes = 1000
tunnel_header = 20
print("Q2 - MOBILE IP REGISTRATION AND TUNNELLING")
for i, event in enumerate(events, 1):
    print(f"{i}. {event}")
print(f"Original packet size: {packet_bytes} bytes")
print(f"Encapsulated packet size: {packet_bytes + tunnel_header} bytes")
print(f"Tunnelling overhead: {tunnel_header} bytes ({tunnel_header/packet_bytes*100:.1f}%)")
print("Result: the Home Agent forwards traffic to the mobile node's current location.")