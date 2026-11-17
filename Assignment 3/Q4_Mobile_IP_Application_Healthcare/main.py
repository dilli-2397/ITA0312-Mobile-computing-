packets = 100
delivered = 98
base_delay_ms = 45
handoff_interruptions = 2
handoff_delay_ms = 120
total_delay = packets * base_delay_ms + handoff_interruptions * handoff_delay_ms
average_delay = total_delay / packets
print("Q4 - MOBILE HEALTHCARE COMMUNICATION")
print("Application: doctor accesses hospital records while moving")
print(f"Packets sent: {packets}")
print(f"Packets delivered: {delivered}")
print(f"Packet delivery ratio: {delivered/packets*100:.1f}%")
print(f"Handoff interruptions: {handoff_interruptions}")
print(f"Estimated average delay: {average_delay:.1f} ms")
print("Requirements: privacy, authentication, reliable delivery and low delay.")
print("Note: illustrative analytical model, not a live network measurement.")