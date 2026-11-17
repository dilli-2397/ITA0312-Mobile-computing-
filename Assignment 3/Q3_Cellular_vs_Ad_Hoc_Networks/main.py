from collections import deque

cellular = {"PhoneA": ["BaseStation"], "BaseStation": ["PhoneA", "Core"], "Core": ["BaseStation", "Server"], "Server": ["Core"]}
adhoc = {"RescueA": ["RescueB"], "RescueB": ["RescueA", "RescueC"], "RescueC": ["RescueB", "Hospital"] , "Hospital": ["RescueC"]}

def reachable(graph, start, target):
    seen, queue = {start}, deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False

print("Q3 - CELLULAR AND AD HOC CONNECTIVITY")
print("Cellular PhoneA -> Server:", "reachable" if reachable(cellular, "PhoneA", "Server") else "unreachable")
print("Ad hoc RescueA -> Hospital:", "reachable" if reachable(adhoc, "RescueA", "Hospital") else "unreachable")
adhoc["RescueB"].remove("RescueC")
adhoc["RescueC"].remove("RescueB")
print("After RescueB-RescueC link failure:", "reachable" if reachable(adhoc, "RescueA", "Hospital") else "unreachable")
print("Finding: cellular uses infrastructure; ad hoc uses peer multi-hop links.")