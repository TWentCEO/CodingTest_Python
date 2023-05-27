
(N, K) = map(int, input().split(" "))

tempList = list(map(int, input().split(" ")))
queue = []

temp_sum = 0

for i in range(K):
    queue.append(tempList[i])
    temp_sum += tempList[i]

temp_max = temp_sum

def tempSum(d: int):
    global temp_sum
    global temp_max
    temp_sum = temp_sum - queue.pop(0) + tempList[d+K-1]
    queue.append(tempList[d+K-1])
    if temp_max < temp_sum:
        temp_max = temp_sum

    # if K % 2 == 0:
    #     for j in range(int(K / 2)):
    #         temp_sum += tempList[d + j] + tempList[d + K - 1 - j]
    # else:
    #     for j in range(int(K / 2)):
    #         temp_sum += tempList[d + j] + tempList[d + K - 1 - j]
    #     temp_sum += tempList[d+int(K / 2)]
    # if temp_max < temp_sum:
    #     temp_max = temp_sum


for i in range(1, N - K+1):
    tempSum(i)

print(temp_max)
