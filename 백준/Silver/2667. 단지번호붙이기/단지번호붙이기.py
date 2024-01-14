N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

count = 0
result = 0
cnt_list = []
    
def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            cnt_list.append(count)
            result += 1
            count = 0
            
cnt_list.sort()
print(result)
for i in cnt_list:
    print(i)
                
            