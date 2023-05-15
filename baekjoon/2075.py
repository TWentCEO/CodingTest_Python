import heapq
N = int(input())

heap = []

for i in range(N):
    n_list = list(map(int,input().split(' ')))
    for n in n_list:
        if len(heap) < N:
            heapq.heappush(heap, n)
            print(heap)
        else:
            if heap[0] < n:
                print(heap)
                heapq.heappop(heap)
                heapq.heappush(heap,n)

print(heap[0])