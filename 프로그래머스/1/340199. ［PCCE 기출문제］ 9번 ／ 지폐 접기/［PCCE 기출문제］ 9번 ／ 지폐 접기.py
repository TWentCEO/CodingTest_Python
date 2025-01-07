
def solution(wallet, bill):
    print(wallet[0])
    max_wallet = max(wallet[0], wallet[1])
    min_wallet = min(wallet[0], wallet[1])
    max_bill = max(bill[0], bill[1])
    min_bill = min(bill[0], bill[1])
    bill = [max_bill, min_bill]

    answer = 0

    while max_bill > max_wallet or min_bill > min_wallet:
        max_bill //= 2
        bill = [max_bill, min_bill]
        max_bill = max(bill[0], bill[1])
        min_bill = min(bill[0], bill[1])
        answer += 1

    return answer




