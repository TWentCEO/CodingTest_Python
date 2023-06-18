from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Bfs(x, y):
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        np = queue.popleft()
        for z in range(4):
            nx = np[0] + dx[z]
            ny = np[1] + dy[z]

            if graph[nx][ny] == 1 and visited[nx][ny] == 0 and 0 < nx < N+1 and 0 < ny < M+1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[np[0]][np[1]] + 1


N, M = map(int, input().split(" "))

graph = [[0 for i in range(M+2)] for j in range(N+2)]

queue = deque()
for i in range(1, N+1):
    List = (list(map(int, input())))
    for n, j in enumerate(List):
        graph[i][n+1] = j

visited = [[0 for i in range(M+2)] for j in range(N+2)]

Bfs(1, 1)
print("\n")
for i in range(N+2):
    print(visited[i])
print(visited[N][M])

