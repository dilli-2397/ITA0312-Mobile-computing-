import math

def array_factor(n, angle):
    theta = math.radians(angle)
    return abs(sum(complex(math.cos(i*math.pi*math.sin(theta)),
                           math.sin(i*math.pi*math.sin(theta))) for i in range(n))) / n

print("Q5 - SDMA ARRAY SIR")
print("Elements | First tested separation meeting 10 dB")
for n in (2, 4, 8, 16):
    found = None
    for angle in range(5, 61, 5):
        sir = -20 * math.log10(max(array_factor(n, angle), 1e-12))
        if sir >= 10:
            found = angle
            break
    print(f"{n} | {found if found is not None else 'not reached'} degrees")
print("Assumptions: half-wavelength spacing, broadside steering, one interferer.")
