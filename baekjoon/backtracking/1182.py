N, S = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

count = 0
store = []


def dfs(start):
    # 만약 더한 수들이 S를 넘을 경우 더 이상 탐색하지 않고 뒤로 간다.
    global count
    if len(store) > 0 and sum(store) == S:
        count += 1

    for i in range(start, N):
        store.append(nums[i])
        dfs(i + 1)
        store.pop()


dfs(0)
print(count)
