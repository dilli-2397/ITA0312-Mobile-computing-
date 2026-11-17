import math
def area(r): return 3*math.sqrt(3)*r*r/2
def erlang_b(c,a):
 b=1.0
 for k in range(1,c+1): b=a*b/(k+a*b)
 return b
def traffic_limit(c,target=.02):
 lo,hi=0.0,2.0*c
 for _ in range(70):
  mid=(lo+hi)/2
  if erlang_b(c,mid)>target: hi=mid
  else: lo=mid
 return (lo+hi)/2
def sir_db(N,n,i0=6): return 10*math.log10((math.sqrt(3*N)**n)/i0)
r=.5; N=7; channels=336//N
print("Q3 - MATHEMATICAL DERIVATIONS")
print("Hex area:",round(area(r),4),"km^2")
print("Cells for 12 km^2:",math.ceil(12/area(r)))
print("Reuse ratio Q:",round(math.sqrt(3*N),3))
print("Channels per cell:",channels)
print("Erlangs at 2% blocking:",round(traffic_limit(channels),2))
print("SIR N=7,n=3.5:",round(sir_db(7,3.5),2),"dB")
print("SIR sanity check N=7,n=4:",round(sir_db(7,4),2),"dB")