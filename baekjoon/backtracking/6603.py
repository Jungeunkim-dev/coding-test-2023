nums = []
while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break
    nums.append(num)

s = []


def solution():
    for i in range(len(nums)):
        dfs(i, 1)
        print("")
        s.clear()


def dfs(case, start):
    if len(s) == 6:
        print(" ".join(map(str, s)))
        return

    # 0번째 원소는 케이스의 개수, 1번째 원소부터 배열 시작
    for i in range(start, nums[case][0] + 1):
        s.append(nums[case][i])
        dfs(case, i + 1)
        s.pop()


solution()
