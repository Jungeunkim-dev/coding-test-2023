def change_chess(chess, x, y):
    black_cnt = 0
    white_cnt = 0
    for i in range(x + 1, 8):
        for j in range(y + 1, 8):
            x_diff = i - x
            y_diff = j - y

            if (x_diff + y_diff) % 2 == 0:
                if chess[i][j] != "W":
                    black_cnt += 1
            elif (x_diff + y_diff) % 2 != 0:
                if chess[i][j] != "B":
                    black_cnt += 1

            if (x_diff + y_diff) % 2 == 0:
                if chess[i][j] != "B":
                    white_cnt += 1
            elif (x_diff + y_diff) % 2 != 0:
                if chess[i][j] != "W":
                    white_cnt += 1

    return min(black_cnt, white_cnt)


N, M = map(int, input().split())

# 체스판 입력받기
chess = []
for i in range(N):
    chess.append(input())

min_changes = []

# 8*8 배열의 체스판을 만드는 경우 모두 완전탐색
for i in range(1, N - 7):
    for j in range(1, M - 7):
        min_changes.append(change_chess(chess, i, j))

print(min_changes)
