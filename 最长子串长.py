class Solution:
    def lengthOfLongestSubstring(self, s):
        l1 = []
        l2 = []
        i = 0
        if s == '':
            return 0
        else:
            while (i < len(s)) and (s[i] not in l1):
                l1.append(s[i])
                i += 1
            if len(l1) >= len(l2):
                l2.clear()
                while (i < len(s)) and (s[i] not in l2):
                    l2.append(s[i])
                    i += 1
            else:
                l1 = l2[:]
                l2.clear()
                while (i < len(s)) and (s[i] not in l2):
                    l2.append(s[i])
                    i += 1
            return len(l1)
