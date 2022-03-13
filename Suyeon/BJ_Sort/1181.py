import sys

N = int(sys.stdin.readline())
words = set()
for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

words = list(words)

words.sort()
words.sort(key=len)


sys.stdout.write("\n".join(words))

