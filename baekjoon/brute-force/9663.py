N = int(input())

isUsed1 = [False for _ in range(40)]
isUsed2 = [False for _ in range(40)]
isUsed3 = [False for _ in range(40)]
cnt = 0


def dfs(count):
    global cnt
    if count == N:
        cnt += 1
        return

    for i in range(N):
        if isUsed1[i] or isUsed2[i + count] or isUsed3[count - i + N - 1]:
            continue

        isUsed1[i] = True
        isUsed2[i + count] = True
        isUsed3[count - i + N - 1] = True
        dfs(count + 1)
        isUsed1[i] = False
        isUsed2[i + count] = False
        isUsed3[count - i + N - 1] = False


dfs(0)
print(cnt)
