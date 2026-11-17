# Q4 - Mobile IP application: mobile healthcare communication
events=[("Hospital ward","Connected",0,20),("Emergency wing","Handoff",1,60),("Ambulance bay","Handoff",1,80),("Remote clinic","Connected",0,25)]
packets=100
lost=sum(e[2] for e in events)*2
delivered=packets-lost
average_delay=sum(e[3] for e in events)/len(events)
print("Q4 - MOBILE HEALTHCARE CONNECTIVITY")
print("Location | Network event | Handoffs | Delay (ms)")
for location,event,handoffs,delay in events:
    print(f"{location} | {event} | {handoffs} | {delay}")
print(f"Packets sent: {packets}")
print(f"Packets lost during handoff (model): {lost}")
print(f"Packets delivered: {delivered}")
print(f"Delivery ratio: {delivered/packets*100:.1f}%")
print(f"Mean event delay: {average_delay:.1f} ms")
print("Requirements: low delay, reliable delivery, secure access and seamless handoff.")
