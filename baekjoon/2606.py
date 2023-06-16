N = int(input())
P = int(input())

List = [[0 for i in range(N + 1)] for j in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0


def dfs(n):
    global cnt
    visited[n] = 1

    for i in range(N + 1):
        if List[n][i] == 1 and visited[i] == 0:
            dfs(i)
            cnt += 1


for i in range(P):
    x, y = map(int, input().split(" "))

    List[x][y] = 1
    List[y][x] = 1

dfs(1)

print(cnt)
