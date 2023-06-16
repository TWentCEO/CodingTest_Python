N = int(input())
step = {}
cnt = 1


def dp(n):
    if n == 1 and n == 2:
        return save[n]
    for i in range(3, n+1):
        save[i] = max(step[i] + step[i-1] + save[i - 3], step[i] + save[i-2])

    return save[n]


for j in range(1, N + 1):
    step[j] = int(input())

if N == 1:
    print(step[1])
elif N == 2:
    print(step[1] + step[2])
else:
    save = {0: 0, 1: step[1], 2: step[1] + step[2]}
    print(dp(N))
