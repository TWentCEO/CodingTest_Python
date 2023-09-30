from collections import deque  

n,k = map(int, input().split())
max_num = 100000
result = [0] * (max_num + 1)

def bfs():
    q = deque()
    
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(result[now])
            break
        for i in (now-1, now+1, now*2):
            if 0 <= i <= max_num and not result[i]:
                result[i] = result[now] + 1
                q.append(i)
                
bfs()
                
