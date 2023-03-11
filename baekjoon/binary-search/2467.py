import sys

input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

min_abs = abs(liquid[-1] + liquid[0])
liq1, liq2 = liquid[-1], liquid[0]


def two_pointer(left, right):
    global liq1, liq2, min_abs
    while left < right:
        current = liquid[left] + liquid[right]

        if abs(current) <= min_abs:
            liq1, liq2 = liquid[left], liquid[right]
            min_abs = abs(current)

        if current > 0:
            right -= 1
        else:
            left += 1


two_pointer(0, N - 1)
print(liq1, liq2)
