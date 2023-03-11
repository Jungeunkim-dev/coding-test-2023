import sys

input = sys.stdin.readline

N, C = map(int, input().split())
home = []
for i in range(N):
    home.append(int(input()))

home.sort()  # 이분탐색 사용하려면 정렬 잊지말기

result = []


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 1  # 일단 끝-시작 1개는 만족하기 때문
        current = home[0]

        # count 추가를 어떻게 해줄 건지 생각
        for i in range(1, N):
            if home[i] - current >= mid:
                cnt += 1
                current = home[i]

        if cnt >= C:
            start = mid + 1
            result.append(mid)
        else:
            end = mid - 1


binary_search(1, home[-1] - home[0])  # st:1, en:끝-시작

print(max(result))

# 랜선 문제랑 동일하게 시작하고 -> 풀어주면 된다
