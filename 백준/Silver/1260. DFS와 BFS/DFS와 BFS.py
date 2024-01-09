from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())

def dfs(grahp, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in grahp[v]:
        if not visited[i]:
            dfs(grahp, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]  = True

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
visited2 = [False] * (n+1)

# 그래프 생성
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(len(graph)):
    graph[i].sort()

# 함수 실행
dfs(graph, v, visited)
print()
bfs(graph, v, visited2)




