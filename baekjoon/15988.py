

T = int(int(input()))

List = [0, 1, 2, 4] + [0] * 999997
for j in range(4, 1000001):
    List[j] = (List[j-1] + List[j - 2] + List[j - 3]) % 1000000009

for i in range(T):
    N = int(input())
    print(List[N])
