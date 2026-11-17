import math
print("Q5 - SCALING AND SENSITIVITY")
for N in [3,4,7,12]:
 q=math.sqrt(3*N); ch=336//N
 row=[round(10*math.log10(q**n/6),2) for n in [2.5,3,3.5,4]]
 print(f"N={N:2} channels/cell={ch:3} SIR dB for n=2.5,3,3.5,4: {row}")
print("Halving cell radius makes cell area one quarter and needs about four times as many cells.")
print("Demand scales linearly with subscriber count: 100,000 users offer 2,500 Erlangs.")
print("A macro-only layout cannot meet long-term demand without densification.")