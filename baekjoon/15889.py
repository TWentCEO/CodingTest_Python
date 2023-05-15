N = int(input())

H = list(map(int,input().split(' ')))
max = 0

if N == 1:
    print("권병장님, 중대장님이 찾으십니다")
    exit()
else:
    R = list(map(int,input().split(' ')))
    for i in range(N-1):
        if max < H[i] + R[i]:
            max = H[i] + R[i]
        if max < H[i+1]:
            print("엄마 나 전역 늦어질 것 같아")
            exit()
print("권병장님, 중대장님이 찾으십니다")