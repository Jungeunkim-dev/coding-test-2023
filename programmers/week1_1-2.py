def solution(bell):
    r = [0 for i in range(len(bell) + 1)]
    g = [0 for i in range(len(bell) + 1)]
    result = []

    for i in range(1, len(bell) + 1):
        if bell[i - 1] == 1:
            r[i] = r[i - 1] + 1
            g[i] = g[i - 1]
        else:
            r[i] = r[i - 1]
            g[i] = g[i - 1] + 1


print(solution([1, 2, 1, 1, 1, 2, 2, 1]))
