distances = input("Enter three distances (miles), separated by spaces ").split(" ")

closest = float(distances[0])
for distance in distances:
    if abs((float(distance) * 1.6) - 15) < abs(closest - 5):
        closest = float(distance)

print("%.2f" % closest)
