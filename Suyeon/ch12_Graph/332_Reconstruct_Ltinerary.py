import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        info = collections.defaultdict(list)

        for ticket in sorted(tickets, reverse=True):
            info[ticket[0]].append(ticket[1])

        for list in info:
            list.sort(reverse=True)

        result = []

        def dfs(start):

            while info[start]:
                dfs(info[start].pop())

            result.append(start)

        dfs('JFK')

        return result



