N = int(input())
x, y = map(int, input().split())
M = int(input())

R = [[0 for i in range(N+1)] for i in range(N+1)]
V = [0 for i in range(N+1)]
cnt = 0
T = -1
for i in range(M):
    a, b = map(int, input().split())
    R[a][b] = 1
    R[b][a] = 1
    
def dfs(n):
    global cnt
    global T
    if n == y:
        T = cnt
        return
    V[n] = 1
    
    for i in range(N+1):
        if R[n][i] == 1 and V[i] == 0:
            cnt += 1
            dfs(i)
            cnt -= 1

dfs(x)
print(T)