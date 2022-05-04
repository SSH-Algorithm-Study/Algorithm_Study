def solution(n, build_frame):
    g_board = [[0] * (n + 1) for _ in range(n + 1)]
    b_board = [[0] * (n + 1) for _ in range(n + 1)]

    answer = []

    def isValidDot(x, y):
        return 0 <= y <= n and 0 <= x <= n

    def isGiOk(x, y):
        if y == 0:  # 바닥일때
            return True

        if isValidDot(x, y - 1) and g_board[x][y - 1]:  # 기둥이 밑에 있을때
            return True

        if b_board[x][y]:  # 보의 왼쪽 끝 위에
            return True

        if isValidDot(x - 1, y) and b_board[x - 1][y]:  # 보의 오른쪽 끝 위에
            return True

        return False

    def isBoOk(x, y):
        if isValidDot(x, y - 1) and g_board[x][y - 1]:
            return True

        if isValidDot(x + 1, y - 1) and g_board[x + 1][y - 1]:
            return True

        if isValidDot(x - 1, y) and b_board[x - 1][y] and isValidDot(x + 1, y) and b_board[x + 1][y]:
            return True

        return False

    for build in build_frame:
        x, y, what, action = build
        if what == 0:  # 기둥
            if action == 1:  # 생성
                g_board[x][y] = 1
                if not isGiOk(x, y):
                    g_board[x][y] = 0
            else:  # 삭제
                g_board[x][y] = 0

                if g_board[x][y + 1]:  # 위에 기둥있다면
                    if not isGiOk(x, y + 1):
                        g_board[x][y] = 1

                if b_board[x][y + 1]:  # 위에 보있다면
                    if not isBoOk(x, y + 1):
                        g_board[x][y] = 1

                if b_board[x - 1][y + 1]:  # 위에 보있다면
                    if not isBoOk(x - 1, y + 1):
                        g_board[x][y] = 1


        else:  # 보
            if action == 1:  # 생성
                b_board[x][y] = 1
                if not isBoOk(x, y):
                    b_board[x][y] = 0
            else:
                b_board[x][y] = 0

                if b_board[x + 1][y]:
                    if not isBoOk(x + 1, y):
                        b_board[x][y] = 1

                if b_board[x - 1][y]:
                    if not isBoOk(x - 1, y):
                        b_board[x][y] = 1

                if g_board[x][y]:
                    if not isGiOk(x, y):
                        b_board[x][y] = 1

                if g_board[x + 1][y]:
                    if not isGiOk(x + 1, y):
                        b_board[x][y] = 1

    for i in range(n + 1):
        for j in range(n + 1):
            if g_board[i][j]:
                answer.append([i, j, 0])
            if b_board[i][j]:
                answer.append([i, j, 1])

    return sorted(answer)


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))