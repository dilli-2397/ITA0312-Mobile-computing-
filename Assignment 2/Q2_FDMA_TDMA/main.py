FDMA_NOMINAL = 2000 // 25
TDMA_CARRIERS = 2000 // 200
TDMA_NOMINAL = TDMA_CARRIERS * 8
FDMA_USABLE = round(FDMA_NOMINAL * 0.95) - 2
TDMA_USABLE = TDMA_CARRIERS * 7

print("Q2 - FDMA AND TDMA CAPACITY MODEL")
print(f"FDMA nominal={FDMA_NOMINAL}, illustrative usable={FDMA_USABLE}")
print(f"TDMA nominal={TDMA_NOMINAL}, illustrative usable={TDMA_USABLE}")
print("Traffic | Requests | FDMA blocked | TDMA blocked")
for name, requests in (("Steady voice", 60), ("Bursty telemetry", 500), ("Synchronized", 200)):
    print(f"{name} | {requests} | {max(0, requests-FDMA_USABLE)} | {max(0, requests-TDMA_USABLE)}")
print("Note: simplified snapshot model; overhead assumptions are illustrative.")
