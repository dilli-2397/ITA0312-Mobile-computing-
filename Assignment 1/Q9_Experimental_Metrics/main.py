metrics=[("Mean SIR","Average radio quality"),("5th percentile SIR","Cell-edge reliability"),("Outage probability","Fraction below 14 dB"),("Blocking probability","Erlang-B or measured blocked calls"),("Sites required","Coverage and deployment cost"),("Handoffs/user-hour","Mobility signalling load"),("Runtime","Simulation efficiency")]
print("Q9 - EXPERIMENTAL METRICS")
for m,d in metrics: print(f"{m}: {d}")
print("Use identical traffic, random seed and user samples for comparisons.")
print("Label each result analytical, simulated or field-measured.")
print("Suggested plots: SIR CDF, blocking vs offered traffic, capacity vs N, sites vs radius.")