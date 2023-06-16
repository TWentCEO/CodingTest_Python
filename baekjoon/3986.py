T = int(input())

result = 0

for i in range(T):
    stack = []
    string = input()

    for j in string:
        if len(stack) == 0:
            stack.append(j)
        else:
            if stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)

    if len(stack) == 0:
        result += 1

print(result)