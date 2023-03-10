import sys

input = sys.stdin.readline

N = int(input())
origin = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

# 이진 탐색을 위해 두 배열 정렬
origin.sort()


def binary_search(key, start, end):
    # 투 포인터 생각
    cnt = 1
    while start <= end:
        mid = (start + end) // 2

        if origin[mid] > key:
            end = mid - 1
        elif origin[mid] < key:
            start = mid + 1
        elif origin[mid] == key:
            next_cnt = mid
            while next_cnt + 1 <= end and origin[next_cnt + 1] == key:
                cnt += 1
                next_cnt += 1
            next_cnt = mid
            while next_cnt - 1 >= start and origin[next_cnt - 1] == key:
                cnt += 1
                next_cnt -= 1
            return cnt

    return 0


for i in range(M):
    print(binary_search(compare[i], 0, N - 1))
