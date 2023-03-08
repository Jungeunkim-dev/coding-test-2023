# 그냥 자연스럽게 생각해봤을 때
# n[i]~n[j]까지 수를 계속 더하기 (sum+=새로운값) 누적해서.
# 이게 왜 DP로 풀어야 하는 문제이지?

# 왜냐하면 만약 그냥 i~j까지 더하기.. 하면 worst case는 O(N^2) 니까.
# 따라서 모든 합을 한번만 구해 주고, 이걸 계속 활용할 수 있게 하려면 누적합을 사용한다.
# i~j까지의 합은 d[j]-d[i-1]를 하면 됨! 이게 점화식!

N, M = map(int, input().split())
nums = list(map(int, input().split()))
result = []

# d[i] => i까지의 누적합
d = [0 for _ in range(100006)]
d[1] = nums[0]

for i in range(2, N + 1):
    d[i] = d[i - 1] + nums[i - 1]


for _ in range(M):
    i, j = map(int, input().split())
    result.append(d[j] - d[i - 1])

for res in result:
    print(res)
