def solution(places):
    answer = []

    def is_valid(room, visited, i, j):
        if not (0 <= i <= 4 and 0 <= j <= 4):
            return False

        if room[i][j] == "X":
            return False

        if visited[i][j]:
            return False

        return True


    def is_ok(room, i, j):
        next = [[i, j, 0]]
        visited = [[0] * 5 for _ in range(5)]

        while next:
            s, t, distance = next.pop()
            visited[s][t] = 1

            if distance < 2:
                if is_valid(room, visited, s - 1, t):
                    if room[s-1][t] == "P":
                        return False
                    next.append([s - 1, t, distance + 1])

                if is_valid(room, visited, s + 1, t):
                    if room[s+1][t] == "P":
                        return False
                    next.append([s + 1, t, distance + 1])

                if is_valid(room,visited, s, t - 1):
                    if room[s][t-1] == "P":
                        return False
                    next.append([s, t - 1, distance + 1])

                if is_valid(room, visited, s, t + 1):
                    if room[s][t+1] == "P":
                        return False
                    next.append([s, t + 1, distance + 1])

        return True

    def is_class_ok(room):
        for i in range(5):
            for j in range(5):
                if room[i][j] == "P":
                    if not is_ok(place,i,j):
                        return 0

        return 1


    for place in places:
        answer.append(is_class_ok(place))


    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))