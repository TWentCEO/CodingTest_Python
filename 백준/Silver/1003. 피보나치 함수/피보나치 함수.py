T = int(input())


for i in range(T):    
    zero = [1, 0]
    one = [0, 1]
    N = int(input())
    if (N > 1):
        for j in range(1, N):
            zero.append(one[-1])
            one.append(one[-1] + one[-2])

    print(zero[N], one[N])