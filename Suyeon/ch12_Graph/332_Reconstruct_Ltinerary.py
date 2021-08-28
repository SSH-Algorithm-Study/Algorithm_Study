import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pairs = collections.defaultdict(list)

        for ticket in tickets:
            pairs[ticket[0]].append(ticket[1])
            if len(pairs[ticket[0]]) > 1 :
                pairs[ticket[0]].sort)_

        result = []
        result.append("JFK")

        while pairs[result[-1]]:
            airport = pairs[result[-1]].pop()
            result.append(airport)





