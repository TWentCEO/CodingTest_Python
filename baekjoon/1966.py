    from queue import deque

    T = int(input())

    for i in range(T):
        result = 0
        Max = 0
        (N, M) = map(int, input().split(" "))

        score = deque(map(int, input().split(" ")))
        target = score[M]
        for j in range(N):
            if Max < score[j]:
                Max = score[j]

        while score:
            if score[0] < Max:
                score.append(score.popleft())
                if M == 0:
                    M = N - 1
                else:
                    M = M - 1
            else:
                if M == 0:
                    for j in range(N):
                        if Max < score[j]:
                            Max = score[j]
                    if target == Max:
                        result += 1
                        break

                score.popleft()
                N = N - 1
                Max = 0

                M = M - 1
                result += 1

                for j in range(N):
                    if Max < score[j]:
                        Max = score[j]

        print(result)
