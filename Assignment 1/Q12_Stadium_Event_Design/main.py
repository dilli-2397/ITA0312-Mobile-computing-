import math
print("Q12 - STADIUM EVENT-DAY DESIGN")
users=50000
traffic_per_user=.025
offered=users*traffic_per_user
area=1.0
radius=.5
cell_area=3*math.sqrt(3)*radius**2/2
cells=math.ceil(area/cell_area)
print("Event users:",users)
print("Offered traffic:",offered,"Erlangs")
print("Event area:",area,"km^2")
print("Baseline macro cell area:",round(cell_area,4),"km^2")
print("Ideal cells to cover event area:",cells)
print("Plan temporary micro/pico cells, sector antennas, backhaul and power.")
print("Use admission control, emergency-service priority and pre-event testing.")