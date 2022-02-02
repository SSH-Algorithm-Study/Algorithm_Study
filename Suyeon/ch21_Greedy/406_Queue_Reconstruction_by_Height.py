import collections

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x : (-x[0],x[1]))
        result = collections.deque()
        stack = []

        for person in people:
            count = person[1]
            while count !=0 and len(result) != 0:
                stack.append(result.popleft())
                count -= 1

            result.appendleft(person)

            while len(stack) != 0:
                result.appendleft(stack.pop())


        return result


