layers=[("Hardware","CPU, RAM, modem, sensors"),("Linux kernel + drivers","Scheduling, memory, drivers, Binder"),("HAL","Vendor hardware interfaces"),("Native libraries/services","Graphics, media, SQLite, TLS, system services"),("ART","DEX verification, JIT/AOT, garbage collection"),("Application framework","Activities, services, permissions, notifications"),("Applications","UI, business logic and data")]
print("4A TASK 1 - ANDROID ARCHITECTURE")
for i,(name,role) in enumerate(layers,1): print(f"{i}. {name}: {role}")
print("Call path: App -> Framework API -> Binder service -> HAL/native code -> Kernel driver")
print("Security: UID sandbox + SELinux + permission checks + Keystore")
print("Power: PowerManager/Doze + kernel suspend/DVFS")