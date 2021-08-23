class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pairs = { "2": ['a','b','c'], "3" : ['d','e','f'], "4": ['g','h','i'], "5": ['j','k','l'],
                  "6": ['m','n','o'], "7": ['p','q','r','s'], "8": ['t','u','v'], "9": ['w','x','y','z']}

        discovered = []
        def dfs(str, i):
            if i > len(digits)-1:
                discovered.append(str)
                return
            for alpha in pairs[digits[i]]:
                 dfs(alpha+str, i+1)

        dfs(str="",i=0)

        return discovered


