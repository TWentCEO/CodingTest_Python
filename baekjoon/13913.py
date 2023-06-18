from collections import deque


def Bfs(s):
    queue = deque([s])
    visited[s] = 1
    while queue:
        n = queue.popleft()
        if n == target:
            return
        for i in range(3):
            if i == 0:
                nx = n - 1
            elif i == 1:
                nx = n + 1
            else:
                nx = 2 * n

            if 0 <= nx < 100001:
                if visited[nx] == 0:
                    queue.append(nx)
                    visited[nx] = visited[n] + 1
                    graph[nx] = n


start, target = map(int, input().split())

graph = [0] * 100001
visited = [0] * 100001


Bfs(start)

print(visited[target] - 1)
answer = [target]
for i in range(1, visited[target]):
    answer.append(graph[answer[-1]])

print(*answer[::-1], sep=' ')
