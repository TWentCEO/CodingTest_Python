N = int(input())
List = list(map(int, input().split(" ")))

result = 0
count = 0


def dp(index, start):
    print("dp",index)
    global count
    max_index = index
    for j in range(start, len(List) - 1):
        if List[max_index] < List[j + 1]:
            print("1번",index, j, List[j+1])
            dp_list.append(List[j+1])
            max_index = j + 1
        else:
            print("2번",index, j, List[j+1])
            if count < len(dp_list):
                count = len(dp_list)
            else:
                break
            for z in range(len(dp_list), 0, -1):
                print(dp_list)
                if dp_list[-1] > List[j+1]:
                    dp_list.pop()
            dp_list.append(List[j+1])


            # if count < len(dp_list):
            #     count = len(dp_list)




if N == 1:
    print(1)


print(List)

for i in range(len(List)):
    dp_list = [List[i]]
    dp(i, i)
    print('--------------')
    print(i, dp_list)
    if result < count:
        result = count


print(result)
