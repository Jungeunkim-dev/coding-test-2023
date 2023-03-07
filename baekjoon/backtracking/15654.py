N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = []


# 수열은 중복될 수 없다
def sequence():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(N):
        if nums[i] not in s:
            s.append(nums[i])
            sequence()
            s.pop()


sequence()
