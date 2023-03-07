def dooms_num(N):
    cnt = 0
    num = 666
    while True:
        string = str(num)
        if "666" in string:
            cnt += 1
        if cnt == N:
            return num
        num += 1


N = int(input())
print(dooms_num(N))
