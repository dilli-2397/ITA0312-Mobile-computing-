import random

random.seed(2026)

def walsh(n):
    h = [[1]]
    while len(h) < n:
        h = [r+r for r in h] + [r+[-x for x in r] for r in h]
    return h

def ber(length, users, mode, count=10000):
    codes = walsh(length)
    errors = 0
    for _ in range(count):
        bits = [random.choice((-1, 1)) for _ in range(users)]
        rx = [0] * length
        for u in range(users):
            code = codes[u]
            amp = 1
            if mode == "random":
                code = [random.choice((-1, 1)) for _ in range(length)]
            if mode == "near-far" and u == 1:
                code = [random.choice((-1, 1)) for _ in range(length)]
                amp = 10
            for j in range(length):
                rx[j] += amp * bits[u] * code[j]
        decision = sum(rx[j] * codes[0][j] for j in range(length))
        if (1 if decision >= 0 else -1) != bits[0]:
            errors += 1
    return errors / count

print("Q3 - CDMA BER SIMULATION (4 USERS)")
print("Code length | Orthogonal BER | Random-code BER | Near-far BER")
for length in (8, 16, 64):
    print(f"{length} | {ber(length,4,'orthogonal'):.4f} | {ber(length,4,'random'):.4f} | {ber(length,4,'near-far'):.4f}")
print("Assumption: synchronous Walsh baseline; random interferers model loss of ideal orthogonality.")
