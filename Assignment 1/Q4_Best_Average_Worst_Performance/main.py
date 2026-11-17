import math
print("Q4 - BEST, AVERAGE AND WORST SIR")
q=math.sqrt(21); n=3.5
base=10*math.log10(q**n/6)
print("Baseline six-interferer estimate:",round(base,2),"dB")
print("Best case: near serving base station; desired signal is strong.")
print("Average case: representative user location and propagation.")
print("Worst case: cell edge/corner; serving path is weaker and interferers may be close.")
loss=10*n*math.log10(1.5)
print("If serving distance increases by 1.5x, desired-link loss:",round(loss,2),"dB")
print("Report mean, median and 5th-percentile SIR; do not infer all users from one mean.")