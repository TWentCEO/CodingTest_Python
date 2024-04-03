from collections import deque

m, n = map(int, input().split(" "))\

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [[0 for i in range(m+2)] for j in range(n+2)]
visited = [[0 for i in range(m+2)] for j in range(n+2)]
for i in range(1, n+1):
    List = (list(map(int, input())))
    for a, j in enumerate(List):
        graph[i][a+1] = j

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while(queue):
        np = queue.popleft()
        for z in range(4):
            nx = np[0]+dx[z]
            ny = np[1]+dx[z]
            if graph[nx][ny] == 1 and visited[nx][ny] == 0 and 0 < nx < n+1 and 0 < ny <m+1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[np[0]][np[1]] + 1

bfs(1,1)
print(visited[n][m])