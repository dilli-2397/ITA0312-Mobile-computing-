
import random
import math
import csv
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(2026)

OUT = "mobile_co2_outputs"
import os
os.makedirs(OUT, exist_ok=True)

def save_csv(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)

print("=" * 65)
print("MOBILE COMPUTING - CO2 ASSIGNMENT 2: SIMULATION OUTPUT")
print("=" * 65)

# Q1: Immediate-send vs store-and-forward
print("\nQ1 - STORE-AND-FORWARD SIMULATION")
q1_rows = []
for p in (0.90, 0.60, 0.30):
    immediate = sum(random.random() < p for _ in range(100))
    queue, delays, delivered, minute = deque(), [], 0, 0
    while delivered < 100:
        if minute < 100:
            queue.append(minute)
        if queue and random.random() < p:
            created = queue.popleft()
            delays.append(minute - created)
            delivered += 1
        minute += 1
    mean_delay = sum(delays) / len(delays)
    delayed = sum(d > 0 for d in delays)
    q1_rows.append([p, immediate, 100-immediate, delivered, delayed, round(mean_delay, 2)])
    print(f"Availability {p:.0%}: immediate delivered={immediate}, lost={100-immediate}; "
          f"queued delivered={delivered}, delayed={delayed}, mean delay={mean_delay:.2f} min")
save_csv("q1_store_forward.csv",
         ["availability","immediate_delivered","immediate_lost","queued_delivered","delayed","mean_delay_min"], q1_rows)
plt.figure()
x = [str(int(r[0]*100))+"%" for r in q1_rows]
plt.bar(x, [r[2] for r in q1_rows], label="Immediate-send lost")
plt.bar(x, [100-r[2] for r in q1_rows], bottom=[r[2] for r in q1_rows], label="Immediate-send delivered")
plt.xlabel("Link availability"); plt.ylabel("Updates out of 100")
plt.title("Q1: Immediate-send delivery and loss")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "Q1_store_forward.png"), dpi=160); plt.close()

# Q2: FDMA / TDMA resource model
print("\nQ2 - FDMA AND TDMA RESOURCE SIMULATION")
fdma_capacity, tdma_capacity = 74, 70
q2_rows = []
for dataset, arrivals in [
    ("Steady voice", [60]*60),
    ("Bursty telemetry", [50 if i % 10 == 0 else 0 for i in range(60)]),
    ("Synchronized arrivals", [200 if i == 0 else 0 for i in range(60)])
]:
    fdma_blocked = sum(max(0, a-fdma_capacity) for a in arrivals)
    tdma_blocked = sum(max(0, a-tdma_capacity) for a in arrivals)
    total = sum(arrivals)
    fdma_util = min(1, total/(60*fdma_capacity))
    tdma_util = min(1, total/(60*tdma_capacity))
    q2_rows.append([dataset,total,fdma_capacity,tdma_capacity,fdma_blocked,tdma_blocked,
                    round(fdma_util*100,2),round(tdma_util*100,2)])
    print(f"{dataset}: requests={total}, FDMA blocked={fdma_blocked}, TDMA blocked={tdma_blocked}, "
          f"FDMA utilization={fdma_util:.1%}, TDMA utilization={tdma_util:.1%}")
save_csv("q2_fdma_tdma.csv", ["dataset","requests","fdma_capacity","tdma_capacity","fdma_blocked",
                               "tdma_blocked","fdma_util_percent","tdma_util_percent"], q2_rows)
plt.figure()
idx = np.arange(3); width = 0.35
plt.bar(idx-width/2, [r[4] for r in q2_rows], width, label="FDMA blocked")
plt.bar(idx+width/2, [r[5] for r in q2_rows], width, label="TDMA blocked")
plt.xticks(idx, ["Steady voice","Bursty data","Synchronized"])
plt.ylabel("Blocked requests"); plt.title("Q2: FDMA vs TDMA blocking")
plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "Q2_fdma_tdma.png"), dpi=160); plt.close()

# Q3: CDMA spreading / despreading
print("\nQ3 - CDMA BER SIMULATION")
def walsh(n):
    H = np.array([[1]])
    while H.shape[0] < n:
        H = np.block([[H,H],[H,-H]])
    return H
q3_rows = []
B = 10000
for L in (8,16,64):
    codes = walsh(L)
    for K in (2, min(4,L), min(8,L)):
        bits = np.random.choice([-1,1], size=(K,B))
        spread = bits[:,:,None] * codes[:K,None,:]
        # Ideal aligned orthogonal case
        rx = spread.sum(axis=0)
        recovered = np.sign((rx * codes[0]).sum(axis=1))
        ber_orth = np.mean(recovered != bits[0])
        # Random non-orthogonal codes
        rand_codes = np.random.choice([-1,1], size=(K,L))
        rand_rx = (bits[:,:,None] * rand_codes[:,None,:]).sum(axis=0)
        rand_dec = np.sign((rand_rx * rand_codes[0]).sum(axis=1))
        ber_random = np.mean(rand_dec != bits[0])
        # Near-far with a one-chip circular shift of a 10x interferer
        nf_rx = spread[0].copy()
        for u in range(1,K):
            # A strong asynchronous interferer is modelled with a non-orthogonal
            # chip sequence, representing loss of ideal code orthogonality.
            strong_code = np.random.choice([-1,1], size=L)
            nf_rx += 10 * bits[u,:,None] * strong_code[None,:]
        nf_dec = np.sign((nf_rx * codes[0]).sum(axis=1))
        ber_nf = np.mean(nf_dec != bits[0])
        q3_rows.append([L,K,ber_orth,ber_random,ber_nf])
        print(f"L={L}, users={K}: BER orthogonal={ber_orth:.4f}, random={ber_random:.4f}, near-far={ber_nf:.4f}")
save_csv("q3_cdma.csv", ["code_length","users","ber_orthogonal","ber_random","ber_near_far"], q3_rows)
plt.figure()
for cond, col in [("Orthogonal",2),("Random",3),("Near-far",4)]:
    plt.plot([r[1] for r in q3_rows if r[0]==64],
             [r[col] for r in q3_rows if r[0]==64], marker="o", label=cond)
plt.xlabel("Number of users (code length 64)"); plt.ylabel("Bit error rate")
plt.title("Q3: CDMA BER comparison (L=64)"); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "Q3_cdma.png"), dpi=160); plt.close()

# Q4: OFDMA scheduling
print("\nQ4 - OFDMA SCHEDULING SIMULATION")
USERS, TONES, RUNS = 8, 64, 1000
q4_rows = []
totals = {"Fixed": [], "Round-robin": [], "Channel-aware": []}
fairness = {"Fixed": [], "Round-robin": [], "Channel-aware": []}
for _ in range(RUNS):
    gain = np.random.exponential(1.0, (USERS, TONES))
    rates = {}
    allocations = {
        "Fixed": [np.arange(u*8,(u+1)*8) for u in range(USERS)],
        "Round-robin": [np.arange(u,TONES,USERS) for u in range(USERS)]
    }
    best = np.argmax(gain, axis=0)
    allocations["Channel-aware"] = [np.where(best==u)[0] for u in range(USERS)]
    for method, alloc in allocations.items():
        user_rates = np.array([sum(math.log2(1+10*gain[u,t]) for t in alloc[u]) for u in range(USERS)])
        total = user_rates.sum()
        jain = (user_rates.sum()**2)/(USERS*(user_rates**2).sum()) if (user_rates**2).sum() else 0
        totals[method].append(total); fairness[method].append(jain)
for method in totals:
    q4_rows.append([method,round(np.mean(totals[method]),3),round(np.mean(fairness[method]),3)])
    print(f"{method}: average sum throughput={np.mean(totals[method]):.3f}, Jain fairness={np.mean(fairness[method]):.3f}")
save_csv("q4_ofdma.csv", ["method","average_sum_throughput","jain_fairness"], q4_rows)
plt.figure()
names = list(totals)
plt.bar(names, [np.mean(totals[n]) for n in names])
plt.ylabel("Average sum throughput (relative units)"); plt.title("Q4: OFDMA scheduling throughput")
plt.tight_layout(); plt.savefig(os.path.join(OUT, "Q4_ofdma.png"), dpi=160); plt.close()

# Q5: SDMA array factor and SIR
print("\nQ5 - SDMA ARRAY SIMULATION")
def array_factor(N, theta_deg, steer_deg=0):
    theta = np.radians(theta_deg); steer = np.radians(steer_deg)
    n = np.arange(N)
    phase = np.pi*(np.sin(theta)-np.sin(steer))
    return abs(np.exp(1j*np.outer(phase,n)).sum(axis=1))/N
angles = np.arange(5,61,5)
q5_rows = []
for N in (2,4,8,16):
    vals = array_factor(N, angles)
    sir = -20*np.log10(np.maximum(vals,1e-12))
    eligible = [int(a) for a,s in zip(angles,sir) if s>=10]
    min_sep = min(eligible) if eligible else "Not reached"
    q5_rows.append([N,min_sep,round(float(np.max(sir)),2)])
    print(f"Array elements={N}: first tested separation meeting 10 dB SIR={min_sep}; max tested SIR={np.max(sir):.2f} dB")
save_csv("q5_sdma.csv", ["array_elements","minimum_separation_deg_for_10db","maximum_tested_sir_db"], q5_rows)
plt.figure()
for N in (2,4,8,16):
    vals = array_factor(N, angles)
    plt.plot(angles, -20*np.log10(np.maximum(vals,1e-12)), marker="o", label=f"N={N}")
plt.axhline(10, linestyle="--", label="10 dB target")
plt.xlabel("Angular separation (degrees)"); plt.ylabel("Approx. SIR (dB)")
plt.title("Q5: SDMA angular separation"); plt.legend(); plt.tight_layout()
plt.savefig(os.path.join(OUT, "Q5_sdma.png"), dpi=160); plt.close()

# Q6: Weighted decision matrix
print("\nQ6 - WEIGHTED TECHNIQUE SELECTION")
weights = np.array([.25,.20,.20,.20,.15])
ratings = {
    "SDMA":[4,3,3,3,2], "TDMA":[3,3,3,4,4], "FDMA":[2,2,3,4,4],
    "CDMA":[4,4,4,3,2], "OFDMA":[5,5,3,5,2]
}
q6_rows = []
for name, vals in ratings.items():
    score = float(np.dot(weights, vals))
    q6_rows.append([name,round(score,3)])
    print(f"{name}: weighted score={score:.3f}")
save_csv("q6_weighted_scores.csv", ["technique","weighted_score"], q6_rows)
plt.figure()
plt.bar([r[0] for r in q6_rows],[r[1] for r in q6_rows])
plt.ylabel("Weighted score (out of 5)"); plt.title("Q6: Multiple-access technique scores")
plt.tight_layout(); plt.savefig(os.path.join(OUT, "Q6_scores.png"), dpi=160); plt.close()

# Q7: Dedicated baseline vs shared pool, 5,000 sensors for 60 minutes
print("\nQ7 - DEDICATED VS SHARED-POOL TELEMETRY")
SENSORS, MINUTES, POOL = 5000, 60, 2500
rng = np.random.default_rng(2026)
generated = rng.random((MINUTES,SENSORS)) < .90
total_reports = int(generated.sum())
# Dedicated: each sensor has a reserved resource; all reports can be sent in the minute.
dedicated_delivered = total_reports
# Shared pool: up to POOL reports per minute; overflow waits in FIFO queue.
queue = deque()
shared_delivered = 0
late = 0
delay_sum = 0
occupied = 0
for minute in range(MINUTES):
    for sensor in np.where(generated[minute])[0]:
        queue.append(minute)
    capacity = POOL
    while queue and capacity:
        created = queue.popleft()
        delay = minute-created
        delay_sum += delay
        if delay > 0:
            late += 1
        shared_delivered += 1
        occupied += 1
        capacity -= 1
# Drain remaining queue after observation window
extra_minute = MINUTES
while queue:
    for _ in range(min(POOL,len(queue))):
        created = queue.popleft()
        delay = extra_minute-created
        delay_sum += delay
        if delay > 0: late += 1
        shared_delivered += 1
        occupied += 1
    extra_minute += 1
mean_delay = delay_sum/shared_delivered if shared_delivered else 0
resource_reduction = (SENSORS-POOL)/SENSORS*100
print(f"Sensors={SENSORS}, observation={MINUTES} min, reports generated={total_reports}")
print(f"Dedicated baseline: resources reserved={SENSORS}, reports delivered={dedicated_delivered}, late=0")
print(f"Shared pool: resources reserved={POOL}, reduction={resource_reduction:.1f}%, "
      f"delivered={shared_delivered}, late beyond 60 s={late}, mean delay={mean_delay:.2f} min")
print("Validation: 50% resource-reduction target met; 99% within-60-second target "
      + ("met." if late <= 0.01*total_reports else "NOT met. Increase pool capacity or stagger reports."))
save_csv("q7_shared_pool.csv",
         ["sensors","minutes","pool_size","generated","dedicated_delivered","shared_delivered",
          "late_reports","mean_delay_min","resource_reduction_percent"],
         [[SENSORS,MINUTES,POOL,total_reports,dedicated_delivered,shared_delivered,late,
           round(mean_delay,3),resource_reduction]])
plt.figure()
plt.bar(["Dedicated","Shared pool"],[SENSORS,POOL])
plt.ylabel("Reserved logical resources"); plt.title("Q7: Resource reservation comparison")
plt.tight_layout(); plt.savefig(os.path.join(OUT, "Q7_resource_comparison.png"), dpi=160); plt.close()

print("\nCSV files and graphs saved in the folder:", OUT)
print("NOTE: These are simplified assignment simulations, not real cellular-network measurements.")
