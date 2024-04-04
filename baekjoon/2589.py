from collections import deque

(m, n) = map(int, input().split())

graph = []

for i in range(m):
    graph.append(list(input()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x, y):  
    queue = deque()
    queue.append((x, y))
    visited = [[0 for i in range(n)] for j in range(m)]
    visited[x][y] = 1
    cnt = 0
    while(queue):
        np = queue.popleft()
        for z in range(4):
            nx = np[0] + dx[z]
            ny = np[1] + dy[z]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 'L' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[np[0]][np[1]] + 1
                    cnt = max(cnt, visited[nx][ny])
    return cnt - 1

result=0
for i in range(m):
  for j in range(n):
    if graph[i][j]=='L':
      result=max(result,bfs(i,j))

print(result)
