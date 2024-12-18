from collections import deque
import sys 

N, M, K, X = list(map(int, sys.stdin.readline().split()))

node_list = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for m in range(M):
    start, end = list(map(int, sys.stdin.readline().split()))
    node_list[start].append(end)

def bfs(start, node_list, visited):
    global K

    queue = deque([start])

    while queue:
        cur_node = queue.popleft()
        if visited[cur_node] == K:
            return
        for node in node_list[cur_node]:
            if visited[node] == 0:
                queue.append(node)
                visited[node] = visited[cur_node] + 1 

bfs(X, node_list, visited)

check = 0
for x in range(2, N+1):
    if visited[x] == K:
        print(x)
        check += 1

if check == 0:
    print(-1)