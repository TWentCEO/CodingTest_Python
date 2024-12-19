from collections import deque
N, M = map(int, input().split())

graph = [[] for i in range(N+1)]

for m in range(M):
    slave, master = map(int, input().split()) 
    graph[master].append(slave)


def bfs(start, graph, N, max_list):
    cnt = 1
    visited = [0 for i in range(N+1)]
    visited[start] = cnt
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for c in graph[cur]:
            if visited[c] == 0:
                queue.append(c)
                cnt += 1
                visited[c] = cnt
    max_list[start] = max(visited)

max_list = [0 for i in range(N+1)]
for n in range(1, N+1):
    bfs(n, graph, N, max_list)

for m in range(1,N+1):
    if max(max_list) == max_list[m]:
        print(m, end=' ')
