print("Q1 - FREQUENCY PLANNING STRATEGIES")
strategies=[
("Fixed reuse","Split 336 channels into N groups; N=7 gives 48 channels/cell. Simple and predictable, but weak for hotspots."),
("Sectorisation","Use directional 120-degree sectors to suppress dominant co-channel interference. Adds antenna and planning complexity."),
("Macro-micro + DCA","Keep macro coverage and add micro-cells at hotspots; dynamically assign channels subject to interference checks.")
]
for name,desc in strategies: print(name+": "+desc)
print("Recommendation: hybrid macro-micro with sectorisation at busy sites.")