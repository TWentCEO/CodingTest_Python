from collections import deque

M, N, H = map(int, input().split())

graph = []
for _ in range(H):
    layer = [list(map(int, input().split())) for _ in range(N)]
    graph.append(layer)

dx = [0, 1, 0, -1, 0, 0]
dy = [1, 0, -1, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def bfs():
    while queue:
        ch, cy, cx = queue.popleft()
        for i in range(6):
            nh, ny, nx = ch + dh[i], cy + dy[i], cx + dx[i]
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if graph[nh][ny][nx] == 0:
                    graph[nh][ny][nx] = graph[ch][cy][cx] + 1
                    queue.append((nh, ny, nx))


queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                queue.append((h, n, m))

bfs()
answer = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 0:
                print(-1)
                exit()
            answer = max(answer, graph[h][n][m])

print(answer - 1)