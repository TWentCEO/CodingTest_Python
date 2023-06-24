from collections import deque

N, M = map(int,input().split(" "))
target = deque(map(int, input().split(" ")))

List = deque([0] * N)
index = 0
result = 0
for i in target:
    List[i-1] = i

while target:
    if List[index] != target[0] and List[-index] != target[0]:
        index += 1
    else:
        if List[index] == target[0]:
            for i in range(index):
                List.append(List.popleft())
                result += 1
            List.popleft()
        elif List[-index] == target[0]:
            for j in range(index):
                List.appendleft(List.pop())
                result += 1
            List.popleft()
        target.popleft()
        index = 0

print(result)