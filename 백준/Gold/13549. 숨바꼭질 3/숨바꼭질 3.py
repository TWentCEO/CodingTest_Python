import heapq

N, K = map(int, input().split())

graph = {i: {} for i in range(100001)}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for next, weight in graph[current_node].items():
            if next < 0 or next > 100000:
                continue
            distance = current_distance + weight

            if distance < distances[next]:
                distances[next] = distance
                heapq.heappush(queue, (distance, next))

    return distances

for i in range(100001):
    if i +1 <= 100000:
        graph[i][i+1] = 1
    if i - 1 >= 0:
        graph[i][i-1] = 1
    if 2 * i <= 100000:
        graph[i][2*i] = 0

answer = dijkstra(graph, N)

print(answer[K])