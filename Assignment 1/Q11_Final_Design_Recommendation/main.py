design={"Coverage":"12 km^2; about 19 ideal macro cells (about 21 with boundary allowance)","Baseline reuse":"N=7; Q=4.583; 48 channels/cell","Propagation":"n=3.5 planning assumption; verify by survey","Radio quality":"14 dB target; baseline estimate about 15.4 dB","Capacity":"Add micro-cells at hostels, lecture halls, library and stadium","Control":"Sectorisation, DCA where supported, admission control and handoff optimisation"}
print("Q11 - RECOMMENDED FINAL DESIGN")
for k,v in design.items(): print(k+": "+v)
print("100,000 subscribers offer 2,500 Erlangs; macro-only capacity is insufficient.")
print("Phase deployment using measured traffic, SIR, site cost and backhaul availability.")