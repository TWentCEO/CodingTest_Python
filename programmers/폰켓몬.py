def solution(nums):
    hash = {}
    answer = 0
    for i in nums:
        if i in hash:
            pass
        else:
            hash[i] = 1
            answer += 1
        if answer >= len(nums)/2:
            return answer
    return answer