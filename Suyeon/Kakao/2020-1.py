import sys


def solution(s):
    answer = sys.maxsize

    def compression(n):
        first = 0
        second = first + n
        count = 0
        result = []
        while second + n - 1 < len(s):
            if s[first:first + n] == s[second:second + n]:
                count += 1
            else:
                if count:
                    result.append(str(count + 1))
                    count = 0
                result.append(s[first:first + n])

            first = second
            second = first + n

        if count:
            result.append(str(count + 1))
        result.append(s[first:])

        return len("".join(result))

    for n in range(1, len(s) // 2 + 1):
        answer = min(compression(n), answer)

    return answer


print(solution("a"))
