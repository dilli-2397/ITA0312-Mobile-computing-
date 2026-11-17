import math
def primes(n):
    count=0
    for x in range(2,n):
        if all(x%d for d in range(2,int(math.sqrt(x))+1)): count+=1
    return count
print("4B TASK 3 - ART BENCHMARK")
print("CPU workload: prime count below 5000 =",primes(5000))
print("Allocation workload: compare bounded and unbounded short-lived objects.")
print("UI workload: render/scroll a large list and record frame timing.")
print("Test compilation modes if supported: verify, speed-profile, speed.")
print("Command: adb shell cmd package compile -m speed-profile -f <package>")
print("Capture GC logs with adb logcat and heap timeline with Android Studio Memory Profiler.")
print("Leak/ANR tests belong in a disposable test build; never force OOM on a personal device.")