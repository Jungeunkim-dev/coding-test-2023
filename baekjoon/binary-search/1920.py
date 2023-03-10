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
    while start <= end:
        mid = (start + end) // 2

        if origin[mid] > key:
            end = mid - 1
        elif origin[mid] < key:
            start = mid + 1
        else:
            return 1

    return 0


for i in range(M):
    print(binary_search(compare[i], 0, N - 1))
