def solution(n, lost, reserve):
    cloth = [1] * (n + 2)  # 체육복의 개수 상태 배열 초기화(1부터 index 시작하므로 n+2로 크기 설정)

    for l in lost:  # 도난당한 경우 -1
        cloth[l] -= 1

    for r in reserve:  # 여벌 옷이 있는 경우 +1
        cloth[r] += 1

    # cloth[i]==2 인 경우 i-1, i+1 학생에게 체육복을 빌려줄 수 있음

    for i in range(1, n + 2):
        if cloth[i] == 0:
            for j in [-1, 1]:
                if cloth[i + j] == 2:
                    cloth[i] += 1
                    cloth[i + j] -= 1
                    break

    return n - (cloth.count(0))
