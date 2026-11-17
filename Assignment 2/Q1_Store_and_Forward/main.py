import random

random.seed(42)
N = 100

print("Q1 - STORE-AND-FORWARD SIMULATION")
print("Availability | Immediate delivered | Lost | Queued delivered | Delayed | Mean delay")
for p in (0.90, 0.60, 0.30):
    immediate = sum(random.random() < p for _ in range(N))
    queue, delays, delivered, minute = [], [], 0, 0
    while delivered < N:
        if minute < N:
            queue.append(minute)
        if queue and random.random() < p:
            created = queue.pop(0)
            delays.append(minute - created)
            delivered += 1
        minute += 1
    print(f"{p:.0%} | {immediate} | {N-immediate} | {delivered} | {sum(d>0 for d in delays)} | {sum(delays)/N:.2f} min")
