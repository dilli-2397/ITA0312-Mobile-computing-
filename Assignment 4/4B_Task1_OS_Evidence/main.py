commands=["adb shell getprop ro.build.version.release","adb shell ps -A","adb shell dumpsys activity processes","adb shell dumpsys meminfo <package.name>","adb shell service list","adb shell cat /proc/<pid>/status"]
print("4B TASK 1 - ANDROID VS IOS EVIDENCE")
print("Android: Linux -> HAL -> native libraries -> ART -> framework -> app; zygote; Binder.")
print("iOS: XNU/Core OS -> Core Services -> Media -> Cocoa Touch; launchd; XPC/Mach ports.")
print("Run on your own emulator/device; output depends on device and OS:")
for c in commands: print("$ "+c)
print("Capture PID, UID, PSS/RSS, process importance, lifecycle and OS version.")
print("This helper does not fabricate live device measurements.")