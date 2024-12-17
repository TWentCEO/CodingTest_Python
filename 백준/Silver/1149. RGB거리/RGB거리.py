N = int(input())
rgb_list = []


for i in range(N):
    rgb_list.append(list(map(int, input().split(" "))))
cost_list = [[0,0,0] for i in range(N)]
cost_list[0] = rgb_list[0]

for j in range(1, N):
    cost_list[j][0] = min(cost_list[j-1][1], cost_list[j-1][2]) + rgb_list[j][0]
    cost_list[j][1] = min(cost_list[j-1][0], cost_list[j-1][2]) + rgb_list[j][1]
    cost_list[j][2] = min(cost_list[j-1][1], cost_list[j-1][0]) + rgb_list[j][2]
    
print(min(cost_list[-1]))