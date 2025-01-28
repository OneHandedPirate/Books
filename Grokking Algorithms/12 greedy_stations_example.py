# O(n**2)
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"},
}

final_stations = set()
count = 0

while states_needed:
    best_station = None
    states_covered = set()

    for station, states in stations.items():
        count += 1
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)
    stations.pop(best_station)


print(final_stations, count, sep="\n")
