class Solution:
    def climbstairs(self, n):
        step = {1: 1, 2: 2}
        for i in range(3, n + 1):
            step[i] = step[i - 1] + step[i - 2]
        return step[n]
