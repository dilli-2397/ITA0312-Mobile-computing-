import math
S=336
def erlang_b(c,a):
 b=1.0
 for k in range(1,c+1): b=a*b/(k+a*b)
 return b
def limit(c,target=.02):
 lo,hi=0.0,2*c
 for _ in range(70):
  m=(lo+hi)/2
  if erlang_b(c,m)>target: hi=m
  else: lo=m
 return (lo+hi)/2
def sir(N,n,i0=6): return 10*math.log10((math.sqrt(3*N)**n)/i0)
print("Q8 - REPRODUCIBLE SIMULATOR BASELINE")
for N in [3,4,7,12]:
 c=S//N
 print(f"N={N}, channels={c}, 2%-blocking traffic={limit(c):.2f} Erlangs, SIR(n=4)={sir(N,4):.2f} dB")
assert round(sir(7,4),1)==18.7
print("Sanity check passed. Extend with seeded user positions, shadowing and antenna patterns.")