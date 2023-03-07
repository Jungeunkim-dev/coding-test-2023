def compare_body(people):
    N = len(people)
    result = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i != j and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                cnt += 1
        result.append(cnt + 1)
    return " ".join(str(s) for s in result)


N = int(input())
people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

print(compare_body(people))
