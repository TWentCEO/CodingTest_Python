N = int(input())
costMax = 0
costSum = 0

dL = [0] * (N + 1)
cL = [0] * (N + 1)


def dp(d: int, cs: int):
    global costMax
    global costSum
    if d + dL[d] > N+1:
        if costMax < cs:
            costMax = cs
    elif d + dL[d] == N+1:
        costSum = cL[d] + cs
        if costMax < costSum:
            costMax = costSum
    else:
        costSum = cL[d] + cs
        tmp = costSum
        for i in range((d+dL[d]), N+1):
            dp(i, tmp)


for i in range(1, N+1):
    D, C = map(int, input().split(" "))

    dL[i] = D
    cL[i] = C

for i in range(1, N + 1):
    if i + dL[i] <= N + 1:
        dp(i, 0)

print(costMax)