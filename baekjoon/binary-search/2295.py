import sys

input = sys.stdin.readline

N = int(input())
U = []
for i in range(N):
    U.append(int(input()))

sums = set()
result = []

for i in range(N):
    for j in range(N):
        sums.add(U[i] + U[j])

for i in range(N):
    for j in range(N):
        if U[j] - U[i] in sums:
            result.append(U[j])

print(max(result))
