weights = [0.25, 0.20, 0.20, 0.20, 0.15]
ratings = {
    "SDMA": [4,3,3,3,2],
    "TDMA": [3,3,3,4,4],
    "FDMA": [2,2,3,4,4],
    "CDMA": [4,4,4,3,2],
    "OFDMA": [5,5,3,5,2]
}

scores = {name: sum(w*r for w,r in zip(weights, row)) for name,row in ratings.items()}
print("Q6 - WEIGHTED ACCESS TECHNIQUE SCORES")
print("Technique | Score out of 5")
for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} | {score:.2f}")
print("Weights: efficiency 25%, scalability 20%, robustness 20%, QoS 20%, simplicity 15%.")
print("Top overall technique:", max(scores, key=scores.get))
