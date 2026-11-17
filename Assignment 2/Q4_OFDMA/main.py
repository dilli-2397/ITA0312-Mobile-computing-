import random
import math

random.seed(2026)
USERS, TONES, RUNS, SNR = 8, 64, 1000, 10
total = {k: [] for k in ("fixed", "round_robin", "channel_aware")}
fairness = {k: [] for k in total}

for _ in range(RUNS):
    gain = [[random.expovariate(1) for _ in range(TONES)] for _ in range(USERS)]
    alloc = {k: [[] for _ in range(USERS)] for k in total}
    for t in range(TONES):
        alloc["fixed"][t//8].append(t)
        alloc["round_robin"][t%USERS].append(t)
        best = max(range(USERS), key=lambda u: gain[u][t])
        alloc["channel_aware"][best].append(t)
    for method in total:
        rates = [sum(math.log2(1+SNR*gain[u][t]) for t in alloc[method][u]) for u in range(USERS)]
        total[method].append(sum(rates))
        fairness[method].append(sum(rates)**2/(USERS*sum(x*x for x in rates)))

print("Q4 - OFDMA SCHEDULING (1000 REALIZATIONS)")
print("Method | Mean sum-rate | Jain fairness")
for method in total:
    print(f"{method} | {sum(total[method])/RUNS:.3f} | {sum(fairness[method])/RUNS:.3f}")
print("Rate model: log2(1 + SNR x gain), normalized bandwidth per tone.")
