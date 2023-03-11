import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
origin = list(map(int, input().split()))
M = int(input())
compare = list(map(int, input().split()))

# 이진 탐색을 위해 두 배열 정렬
origin.sort()


# bisect 함수 이용해서 해결
def count_bisect(key):
    right_index = bisect_right(origin, key)
    left_index = bisect_left(origin, key)
    return right_index - left_index


for num in compare:
    print(count_bisect(num), end=" ")
