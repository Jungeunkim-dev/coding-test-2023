N, M = list(map(int, input().split()))
s = []


def sequence():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            sequence()
            s.pop()


sequence()
