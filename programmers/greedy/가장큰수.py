def solution(numbers):
    # numbers 내 num -> 2차원 배열로 변환

    numbers_arr = [[-1] * 4 for _ in range(len(numbers))]

    for i in range(len(numbers)):
        j = 0
        for s in str(numbers[i]):
            numbers_arr[i][j] = int(s)
            j += 1

    numbers_arr = sorted(numbers_arr, key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

    answer = ""

    for i in range(len(numbers)):
        j = 0
        while numbers_arr[i][j] != -1:
            answer += str(numbers_arr[i][j])
            j += 1

    print(answer)


solution([6, 10, 2])
