import heapq

N, D = map(int, input().split())

graph = {i:{} for i in range(D+1)}


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance < distances[current_node]:
            continue

        for next, weight in graph[current_node].items():
            if next <= D:
                distance = current_distance + weight

                if distance < distances[next]:
                    distances[next] = distance
                    heapq.heappush(queue, (distance, next))
    return distances



for i  in range(D):
    graph[i][i+1] = 1

for n in range(N):
    s, e, w = map(int, input().split())
    if s<=D and e<=D and w <= D:
        graph[s][e] = min(graph[s].get(e, float('inf')), w)

answer = dijkstra(graph, 0)[D]

print(answer)