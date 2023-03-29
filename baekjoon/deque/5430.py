from collections import deque

T = int(input())
result = []

for _ in range(T):
    p = input()
    n = int(input())

    x = input()

    if n == 0:
        if "D" in p:
            result.append("error")
        else:
            result.append([])
        continue

    x = x.replace("[", "")
    x = x.replace("]", "")

    x = list(map(int, x.split(",")))

    q = deque(x)

    st = 0  # 짝수면 오른쪽--> // 홀수면  <-- 왼쪽 에서 읽어준다.
    error = False

    for i in range(len(p)):
        if p[i] == "R":  # reverse
            st += 1

        elif p[i] == "D":  # delete
            if not q:
                error = True
                break
            if st % 2 == 0:  # 맨 왼쪽 원소 빼주기
                q.popleft()
            else:  # 맨 오른쪽 원소 빼주기
                q.pop()

    if not error:
        if st % 2 == 0:
            result.append(list(q))
        else:
            q.reverse()
            result.append(list(q))
    else:
        result.append("error")

for r in result:
    print(r)
