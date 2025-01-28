# O(V + E) where V - quantity of nodes and E - quantity of edge

from collections import deque
from random import choices, randint
from string import ascii_lowercase as letters


def graph_filling(g: dict, node_list: list, depth: int) -> None:
    if depth < 2:
        return

    for name in node_list:
        g[name] = ["".join(choices(letters, k=8)) for _ in range(randint(2, 6))]
        graph_filling(g, g[name], depth - 1)


def is_seller(s: str) -> bool:
    return s.endswith("dima")


def search(graph: dict, name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    checked = []
    n = 0
    while search_queue:
        n += 1
        person = search_queue.popleft()
        if person not in checked:
            if is_seller(person):
                print("Found one!", person, f"Checks: {n}", sep="\n")
                return True
            else:
                if graph.get(person):
                    search_queue += graph[person]
                    checked.append(person)
    print("Not found :(", f"Checks: {n}", sep="\n")
    return False


graph = {"me": ["".join(choices(letters, k=8)) for i in range(randint(2, 6))]}

while True:
    try:
        _max = int(input("Введите глубину графа: "))
    except ValueError:
        print("Некорректный ввод!")
    else:
        break


graph_filling(graph, graph["me"], _max)
# pprint(graph)
print("Graph is filled!\n")

search(graph, "me")
