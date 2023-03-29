import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [[False] * (N) for _ in range(N)]  # False N*N 배열로 초기화
M = int(input())
result = []  # 리턴할 결과 함수

# 팰린드롬 값 구하기

# 1. 각 1자리 값들은 모두 True
for i in range(N):
    dp[i][i] = True

for i in range(1, N):  # end의 값
    for j in range(0, i):
        if nums[i] == nums[j]:
            if i - j == 1:  # start 와 end가 1차이날때
                dp[j][i] = True

            else:
                if dp[j + 1][i - 1] == True:
                    dp[j][i] = True
                else:
                    dp[j][i] = False

        else:
            dp[j][i] = False

for _ in range(M):
    S, E = map(int, input().split())
    result.append(dp[S - 1][E - 1])

for r in result:
    print(int(r))
