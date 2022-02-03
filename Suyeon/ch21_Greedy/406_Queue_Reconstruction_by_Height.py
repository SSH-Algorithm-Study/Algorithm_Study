import collections

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x : (-x[0],x[1])) # 키에 대해서는 내림차순 앞에 있는 사람수에 대해서는 내림차순
        result = collections.deque()
        stack = []

        for person in people:
            count = person[1]

            # 앞에서 부터 pop
            while count !=0 and len(result) != 0:
                stack.append(result.popleft())
                count -= 1

            # 적당한 자리에 넣어주기
            result.appendleft(person)

            # 앞에 pop한거 다시넣어주기
            while len(stack) != 0:
                result.appendleft(stack.pop())


        return result



class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))  # 키에 대해서는 내림차순 앞에 있는 사람수에 대해서는 내림차순
        result = []

        for person in people:
            result.insert(person[1], person)

        return result