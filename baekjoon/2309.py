list = []
visited = [0] * 9
total = 0
count = 0
result = []

def dfs(start: int, depth: int, sum: int) : 
    global count
    global total
    if (depth == 6 and sum == 100):
        total = sum
        count = depth
        for i in range(len(visited)):
            if visited[i] == 1:
                result.append(list[i])

    for i in range(start + 1, 9):
        if (count == 6 and total == 100): break
        elif (depth <= 6 and sum + list[i] <= 100):
            visited[i] = 1
            dfs(i, depth+1, sum + list[i])
            visited[i] = 0

for i in range(9):
    list.append(int(input()))

list.sort()

for i in range(len(list)):
    visited[i] = 1
    dfs(i, 0, list[i])
    if (len(result) == 7): break
    else: visited[i] = 0
    

for i in range(len(result)) :
    print(result[i])