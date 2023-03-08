T = int(input())

d = [0 for _ in range(15)]
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 13):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]


for i in range(T):
    idx = int(input())
    print(d[idx])
