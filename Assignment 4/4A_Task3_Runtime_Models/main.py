steps=["Launcher requests Activity","ActivityTaskManager resolves package","Zygote forks isolated app process","ART maps/verifies DEX and initialises heap","Application object is created","Activity callbacks run","Views are measured and laid out","Renderer submits first frame"]
print("4A TASK 3 - RUNTIME AND APP LAUNCH")
for i,s in enumerate(steps,1): print(f"{i}. {s}")
print("Android: DEX; ART interpreter/JIT/profile-guided AOT; managed heap and GC.")
print("iOS: native Mach-O; Objective-C runtime; ARC reference counting.")
print("Windows: native PE or managed .NET assembly; CLR JIT for managed code.")
print("Cold start creates process/runtime; warm start may reuse a live process.")