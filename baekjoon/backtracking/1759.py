L, C = map(int, input().split())
passwords = list(map(str, input().split()))
passwords.sort()

s = []

moums = {"a": "0", "e": "0", "i": "0", "o": "0", "u": "0"}


# 1개 이상의 모음과 2개 이상의 자음이 보장되는지 확인
def checkMoum(arr):
    moum = 0

    for i in range(len(arr)):
        if arr[i] in moums:
            moum += 1

    if moum >= 1 and (len(arr) - moum) >= 2:
        return True
    else:
        return False


def dfs(start):
    if len(s) == L and checkMoum(s):
        print("".join(map(str, s)))
        return

    for i in range(start, C):
        s.append(passwords[i])
        dfs(i + 1)
        s.pop()


dfs(0)
