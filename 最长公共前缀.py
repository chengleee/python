class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest=min(strs,key=len)
        for x, y in enumerate(shortest):
            for s in strs:
                if s[x]!=y:
                    return shortest[:x]
        return shortest
