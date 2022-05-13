import collections

# 인접단어찾기
def oneDiff(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count == 1


def solution(begin, target, words):
    route = collections.defaultdict(list)

    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if oneDiff(words[i], words[j]):
                route[words[i]].append(words[j])
                route[words[j]].append(words[i])

    queue = []
    distance = {}  # 방문여부와 길이 한번에 체크
    for word in words:
        if oneDiff(word, begin):
            queue.append([word, 1])
            distance[word] = 1

    while queue:
        w, count = queue.pop(0)
        for nextWord in route[w]:
            if nextWord not in distance:
                queue.append([nextWord, count + 1])
                distance[nextWord] = count + 1

    return distance.get(target, 0) # get으로 요소 없을 때 가져올 수 있음 