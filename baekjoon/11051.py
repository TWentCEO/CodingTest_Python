N, K = map(int, input().split(" "))

nmk = N - K
top = 1
bottom = 1
for i in range(N, K, -1):
    top *= i
for j in range(1, N-K+1):
    bottom *= j

result = int((top // bottom) % 10007)


print(int(result))