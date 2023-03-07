N, M = map(int, input().split())
s = []


def sequence(start):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(start, N + 1):
        s.append(i)
        sequence(i)
        s.pop()


sequence(1)
