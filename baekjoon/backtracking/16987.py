N = int(input())
eggs = []
result = []

for i in range(N):
    s, w = map(int, input().split())
    eggs.append((s, w))


def dfs(start):
    for i in range(start, N - 1):
        if eggs[i][0] < 0:
            continue

        eggs[i][0] -= eggs[i + 1][1]
        eggs[i + 1][0] -= eggs[i][1]

        dfs(i + 1)

        eggs[i][0] += eggs[i + 1][1]
        eggs[i + 1][0] += eggs[i][1]

def checkEggs():
  cnt = 0 
  for i in range(cnt):
    