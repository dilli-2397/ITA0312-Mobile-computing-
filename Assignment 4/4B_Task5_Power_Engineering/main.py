techniques=[("DVFS","CPU load/thermal state","Lower voltage/frequency; longer task latency"),("Doze/App Standby","Screen off, stationary, unplugged","Defer background network/jobs"),("Batching/WorkManager","Queue threshold and job window","Fewer radio wakeups; later delivery")]
print("4B TASK 5 - POWER ENGINEERING")
for n,t,e in techniques: print(f"{n} | Trigger: {t} | Effect: {e}")
print("Measure: adb shell dumpsys batterystats --reset")
print("Run fixed workload, then: adb shell dumpsys batterystats")
print("Compare wakeup alarms, wakelock duration, radio active time, GPS and estimated mAh.")
print("Stress case: continuous partial wakelock reduces deep-sleep/Doze benefit.")
print("Let the OS scheduler choose heterogeneous CPU cores.")