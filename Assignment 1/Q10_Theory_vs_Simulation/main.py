print("Q10 - THEORY VS SIMULATION")
differences=[("Geometry","Theory uses equal-distance first-tier interferers; simulation uses actual distances."),("Propagation","Theory uses one path-loss exponent; simulation can add shadowing, fading and buildings."),("Traffic","Erlang-B assumes random arrivals and no queue; real traffic may be bursty."),("Antennas","Ideal sector model ignores side lobes, reflections and overlap."),("Mobility","Handoffs and reserved channels can change blocking and packet loss.")]
for a,b in differences: print(a+": "+b)
print("Validate code with N=7,n=4 SIR = 18.66 dB (about 18.7 dB).")
print("Explain error sources and whether they change the design choice.")