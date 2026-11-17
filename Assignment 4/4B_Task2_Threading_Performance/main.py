workloads=[("Large JSON/image task","Worker pool should protect UI responsiveness"),("Tiny 2 KB JSON task","Synchronous path may beat thread dispatch"),("Shared locked map","Lock contention can erase parallelism")]
print("4B TASK 2 - MAIN THREAD VS BACKGROUND WORK")
for n,r in workloads: print(f"{n}: {r}")
print("Architecture: UI -> ViewModel -> UseCase -> Repository -> bounded Executor/coroutine")
print("Measure at least 5 runs: elapsed time, CPU time, frame time, thread count, PSS and context switches.")
print("Background execution improves responsiveness, not necessarily total computation time.")
print("Reuse bounded workers; avoid creating a new thread per tiny operation.")