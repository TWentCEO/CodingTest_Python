import sys
sys.setrecursionlimit(100000)

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]


def dfs(x, y, X, Y):
    global visited
    global Map

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if Map[nx][ny] == 1 and visited[nx][ny] == 0 and 0 < nx < X+1 and 0 < ny < Y+1:
            visited[nx][ny] = 1
            dfs(nx, ny, X, Y)


while True:
    W, H = map(int, input().split(" "))

    if W == 0 and H == 0:
        break

    Map = [[0 for j in range(W + 2)] for i in range(H + 2)]
    visited = [[0 for j in range(W + 2)] for i in range(H + 2)]
    cnt = 0
    for i in range(1, H+1):
        List = list(map(int, input().split(" ")))

        for n, j in enumerate(List):
            Map[i][n + 1] = j

    for i in range(1, H+1):
        for j in range(1, W+1):
            if Map[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j, H, W)
                cnt += 1

    print(cnt)
