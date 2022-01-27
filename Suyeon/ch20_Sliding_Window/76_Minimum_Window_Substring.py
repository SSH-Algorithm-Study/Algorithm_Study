import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0

        freqs = collections.Counter(t)
        substr = collections.defaultdict(int)

        result = ""

        def check(substr):
            for key in freqs.keys():
                if substr[key] < freqs[key]:
                    return False
            return True


        while right < len(s) :
            print(s[left:right + 1])
            substr[s[right]] += 1
            if not check(substr):
                right += 1
            else:
                result = s[left:right+1]
                break

        while right < len(s)-1 :
            print(s[left:right+1])
            if check(substr):
                result = s[left:right + 1]
                substr[s[left]] -= 1
                left += 1
            else:
                substr[s[left]] -= 1
                left += 1
                right += 1
                substr[s[right]] += 1

        if check(substr):
            while left <= right:
                print(s[left:right + 1])
                if check(substr):
                    print("hello")
                    substr[s[left]] -= 1
                    left += 1
                else:
                    result = s[left-1 :right + 1]
                    break

        return result


sol = Solution()
print(sol.minWindow(s = "AAA", t = "AA"))






