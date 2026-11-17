# Q3 - Cellular and ad hoc network connectivity comparison
cellular={"Mobile-A":["Base-Station"],"Base-Station":["Core-Network"],"Core-Network":["Server"]}
adhoc={"Mobile-A":["Node-B"],"Node-B":["Node-C"],"Node-C":["Server"]}
def path(graph,start,target):
    queue=[(start,[start])]
    seen={start}
    while queue:
        node,route=queue.pop(0)
        if node==target: return route
        for nxt in graph.get(node,[]):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt,route+[nxt]))
    return []
print("Q3 - CELLULAR VS AD HOC NETWORK")
for name,graph in (("Cellular",cellular),("Ad hoc",adhoc)):
    route=path(graph,"Mobile-A","Server")
    print(f"{name} path: {' -> '.join(route)}")
    print(f"{name} hops: {len(route)-1}")
print("Cellular: infrastructure and base station required.")
print("Ad hoc: nodes forward packets without fixed base-station infrastructure.")
print("Disaster case: ad hoc communication remains possible if relay nodes form a connected path.")
