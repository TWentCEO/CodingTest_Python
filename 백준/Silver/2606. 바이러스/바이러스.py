n = int(input())
m = int(input())

list = [[0 for i in range(n+1)] for j in range(n+1)]
visited = [0] * (n + 1)
cnt = 0

for i in range(m):
	a, b =map(int, input().split(" "))
	list[a][b] = 1
	list[b][a] = 1

def dfs(x):
	global cnt
	visited[x] = 1
	for i in range(n+1):
		if list[x][i] == 1 and visited[i] == 0:
			dfs(i)
			cnt += 1

dfs(1)
print(cnt)