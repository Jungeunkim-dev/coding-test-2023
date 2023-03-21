def convert_time(time):
    h, m = map(int, time.split(":"))  # hh:mm 을 변환
    return h * 60 + m


def solution(booked, unbooked):
    # 시간을 int 형식으로 변환
    booked = [(convert_time(t), name) for t, name in booked] + [(1000000, None)]
    unbooked = [(convert_time(t), name) for t, name in unbooked] + [(1000000, None)]
    booked.sort()
    unbooked.sort()

    booked_idx, unbooked_idx, t, answer = 0, 0, 0, []  # 각 index 값을 0으로 초기화

    while booked_idx < len(booked) and unbooked_idx < len(unbooked):
        t1, t2 = booked[booked_idx][0], unbooked[unbooked_idx][0]

        if t1 <= t:
            answer.append(booked[booked_idx][1])  # 해당 index의 이름을 정답 배열에 추가
            booked_idx += 1
            t += 10  # 10분 경과시킴

        elif t2 <= t:
            answer.append(unbooked[unbooked_idx][1])  # 해당 index의 이름을 정답 배열에 추가
            unbooked_idx += 1
            t += 10

        else:  # 최초일 경우
            t = min(t1, t2)

    answer.pop()
    return answer


print(
    solution([["09:55", "hae"], ["10:05", "jee"]], [["10:04", "hee"], ["14:07", "eom"]])
)
