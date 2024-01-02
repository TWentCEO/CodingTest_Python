n = int(input())

d = {1:0}

def dp(n):
    if n in d.keys():
        return d[n]
    if (n % 2 == 0) and (n % 3 == 0):
        d[n] = min(dp(n//2)+1, dp(n//3)+1)
    elif (n % 3 == 0):
        d[n] = min(dp(n//3)+1, dp(n-1)+1)
    elif (n % 2 == 0):
        d[n] = min(dp(n//2)+1, dp(n-1)+1)
    else:
        d[n] = dp(n-1)+1
    return d[n]

print(dp(n))