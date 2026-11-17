states=[("Active","Screen on/user interaction","Foreground UI; short bounded work"),("Idle","Screen off/no interaction","Batch jobs and limited sampling"),("Doze/Suspended","Stationary, unplugged, screen off","System wake events; defer app network work"),("Charging","Power connected","Batch sync, backup and maintenance")]
print("4A TASK 5 - POWER STATE POLICY")
for s,e,w in states: print(f"{s} | Entry: {e} | Work: {w}")
print("Urgent push: system push service receives event; do not hold permanent wakelock.")
print("At 15% battery: increase stationary sampling interval, batch uploads, defer non-urgent work.")
print("Emergency exception: visible, time-limited foreground operation with bounded wake time.")