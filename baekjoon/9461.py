T = int(input())

for i in range(T):
    result = 0
    N = int(input())

    List = [0,1,1,1]
    if N == 1 or N == 2 or N == 3:
        print(1)
    else:
        for j in range(4,N+1):
            result = List[j-3] + List[j-2]
            List.append(result)

    print(List[-1])