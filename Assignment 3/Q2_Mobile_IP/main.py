# Q2 - Mobile IP registration and tunnelling simulation
packets=50
payload_bytes=200
tunnel_header_bytes=20
registration_delay_ms=120
handoff_interrupt_ms=40
extra_bytes=packets*tunnel_header_bytes
print("Q2 - MOBILE IP REGISTRATION AND PACKET DELIVERY")
print(f"Packets sent: {packets}")
print(f"Payload per packet: {payload_bytes} bytes")
print(f"Encapsulation overhead: {tunnel_header_bytes} bytes per packet")
print(f"Total tunnel overhead: {extra_bytes} bytes")
print(f"Total tunneled bytes: {packets*(payload_bytes+tunnel_header_bytes)} bytes")
print(f"Registration delay (model input): {registration_delay_ms} ms")
print(f"Handoff interruption (model input): {handoff_interrupt_ms} ms")
print(f"Combined mobility interruption: {registration_delay_ms+handoff_interrupt_ms} ms")
print("Flow: MN obtains CoA -> sends registration -> HA updates binding -> HA tunnels packets to CoA.")
