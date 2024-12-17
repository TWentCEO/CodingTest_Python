from collections import deque 
a, b = map(int,(input().split()))

def bfs(a, b):
    queue = deque([(a, 1)])

    while (queue):
        cur, cnt = queue.popleft()
        if cur == b:
            print(cnt)
            return
        else:
            if cur * 2 <= b:
                queue.append((cur*2, cnt+1))
            if cur * 10 + 1 <= b:
                queue.append((cur * 10 + 1, cnt+1))
    print(-1)
bfs(a, b)