def solution(storey):
    num = list(map(int, str(storey)))
    cnt = 0
    for i in range(len(num) - 1, -1, -1):
        if i == 0:
            if num[i] <= 5:
                cnt += num[i]
            else:
                cnt += 10 - num[i] + 1
        else:
            if num[i] >= 10:
                num[i - 1] += 1
                num[i] = 10 - num[i]

            if num[i] <= 5:
                cnt += num[i]
            else:
                num[i - 1] += 1
                cnt += 10 - num[i]

    return cnt


solution(2554)
