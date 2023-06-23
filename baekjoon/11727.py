N = int(input())

List = [1, 1, 3, 5]
Sum = 0
if N == 1:
    print(1 % 10007)
elif N == 2:
    print(3 % 10007)
elif N == 3:
    print(5 % 10007)
else:
    for i in range(3, N):
        Sum = List[i] + 2 * List[i - 1]
        List.append(Sum)

    print(List[-1] % 10007)
