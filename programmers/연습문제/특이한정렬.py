def solution(numlist, n):
    answer = []
    s = []  # 스택 선언

    numlist.sort()

    for num in numlist:
        while s and abs(n - num) > s[-1][1]:
            answer.append(s[-1][0])
            s.pop()
        s.append((num, abs(n - num)))

    while s:
        answer.append(s[-1][0])
        s.pop()
    return answer
