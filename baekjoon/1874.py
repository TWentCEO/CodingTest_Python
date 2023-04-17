n = int(input())
cur = 1
stack = []
answer = []
flag = 0
for i in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1
    
    if num == stack[-1]:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)

