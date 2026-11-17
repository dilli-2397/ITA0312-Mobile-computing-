import random
from collections import deque
from statistics import mean

random.seed(2026)
SENSORS, MINUTES, POOL = 5000, 60, 2500
arrivals = []
for minute in range(MINUTES):
    count = sum(random.random() < 0.90 for _ in range(SENSORS))
    arrivals.append([minute] * count)

queue, delays = deque(), []
for minute in range(MINUTES):
    queue.extend(arrivals[minute])
    for _ in range(min(POOL, len(queue))):
        delays.append(minute - queue.popleft())

extra_minute = MINUTES
while queue:
    for _ in range(min(POOL, len(queue))):
        delays.append(extra_minute - queue.popleft())
    extra_minute += 1

generated = sum(map(len, arrivals))
late = sum(delay > 1 for delay in delays)
print("Q7 - DEDICATED VS SHARED-POOL TELEMETRY")
print(f"Sensors: {SENSORS}; observation: {MINUTES} minutes")
print(f"Generated and delivered reports: {generated}")
print(f"Dedicated resources: {SENSORS}")
print(f"Shared-pool resources: {POOL}; reduction: {(1-POOL/SENSORS)*100:.1f}%")
print(f"Reports delayed beyond 60 seconds: {late}")
print(f"Mean delivery delay: {mean(delays):.2f} minutes")
print("The 50% resource target is reached, but the 99% within-60-second target is not.")
