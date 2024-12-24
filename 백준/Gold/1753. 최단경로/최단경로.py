import heapq, sys

input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input())
graph = [[] for _ in range(V+1)]

def dijkstra(graph, start):
    distances = [float("inf")] * (V+1)
    queue = [(0, start)]
    distances[start] = 0

    while queue:
        cur_dis, cur_node = heapq.heappop(queue)

        if distances[cur_node] < cur_dis:
            continue

        for next, weight in graph[cur_node]:
            distance = cur_dis + weight
            if distance < distances[next]:
                distances[next] = distance
                heapq.heappush(queue, (distance, next))

    return distances

for e in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

answer = dijkstra(graph, start)

for i in range(1, V+1):
    if answer[i] == float("inf"):
        print("INF")
    else:
        print(answer[i])