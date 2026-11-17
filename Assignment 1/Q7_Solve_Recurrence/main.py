import math
print("Q7 - SOLVING THE RECURRENCE")
for ratio in [4,8,16,32,64]:
 k=math.ceil(math.log(ratio,4))
 print(f"Demand/capacity={ratio}: split rounds={k}; growth factor={4**k}")
print("Formula: k = ceil(log_4(D/C0))")
print("Example: demand 8x baseline -> 2 rounds -> 16x cell count in split footprint.")
print("Selective splitting with constant f uses growth factor g=1+3f.")