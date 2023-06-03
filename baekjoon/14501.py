N = int(input())
costMax = 0
costSum = 0

dL = [0] * (N + 1)
cL = [0] * (N + 1)


def solution(d: int, cs: int):
    global costMax
    global costSum
    print(d, cs)
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
            solution(i, tmp)


for i in range(1, N+1):
    D, C = map(int, input().split(" "))

    dL[i] = D
    cL[i] = C

print("dL", dL, "\n", "cL", cL)

for i in range(1, N + 1):
    if i + dL[i] <= N + 1:
        print("day:", i)
        solution(i, 0)
        print("costMax:", costMax)
print(costMax)