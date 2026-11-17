def policy(battery,network,motion,emergency=False):
    if emergency: return (2,"priority upload")
    if network=="OFFLINE": return (30 if motion=="MOVING" else 300,"encrypted queue")
    if battery<15 and motion=="STATIONARY": return (300,"defer until charging")
    if battery<=30 and network=="LTE": return (120,"defer unless threshold")
    if network=="WIFI": return (10,"batch every 2 min")
    if network=="LTE": return (15,"batch every 5 min")
    return (60,"defer")
cases=[("Normal Wi-Fi moving",80,"WIFI","MOVING",False),("Low LTE stationary",20,"LTE","STATIONARY",False),("Offline moving",60,"OFFLINE","MOVING",False),("Emergency",45,"WIFI","MOVING",True),("Critical offline",12,"OFFLINE","STATIONARY",False)]
print("4B TASK 6 - BATTERY-AWARE POLICY SIMULATION")
print("Scenario | Battery | Network | Motion | Interval(s) | Upload")
for name,b,n,m,e in cases:
    interval,upload=policy(b,n,m,e)
    print(f"{name} | {b}% | {n} | {m} | {interval} | {upload}")
print("Security: encrypt before local persistence; authenticate + TLS before upload; ACK before marking synced.")
print("Test thresholds 30%, 15%, offline, unknown motion and emergency override.")
print("Energy values are not measured; calibrate coefficients using Battery Historian on target hardware.")
print("Emergency fleet of 5000 devices needs priority queues, back-pressure, time limits and audit.")