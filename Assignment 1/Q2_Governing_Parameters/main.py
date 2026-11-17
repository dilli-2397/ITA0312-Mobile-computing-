params={"Township area":"12 km^2","Spectrum":"336 duplex channels","Cluster size N":7,"Cell radius":"0.5 km (planning assumption)","Path-loss exponent n":3.5,"SIR target":"14 dB","Traffic per user":"0.025 Erlang","Blocking target":"2%"}
print("Q2 - GOVERNING DESIGN PARAMETERS")
for k,v in params.items(): print(f"{k}: {v}")
print("Trade-off: larger N increases reuse distance/SIR but reduces channels per cell.")
print("Trade-off: smaller radius increases site count and handoff rate.")