N = int(input())

triangle = [[0 for j in range(N)]for i in range(N)]
dp = [[0 for j in range(N)]for i in range(N)]

for i in range(N):
    sub_list = list(map(int, input().split(" ")))
    for j in range(len(sub_list)):
        triangle[i][j] = sub_list[j]

if N == 1:
    print(triangle[0][0])
elif N == 2:
    print(max(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1]))
else:
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

    for i in range(2, N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][0]
            elif j == i:
                dp[i][j] = dp[i-1][i-1] + triangle[i][j]
            else:
                for z in range(2):
                    if z == 0:
                        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                    if z == 1:
                        dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])
    print(max(dp[N-1]))