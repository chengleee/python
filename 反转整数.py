"""class Solution:
    def reverse(self, x):
        if not(((-2) ** 31) < x < (2 ** 31 - 1)):
            return 0
        else:
            oldx = x
            if x < 0:
                x = -x
            i = 0
            newx = 0
            s = []
            s.append(x % 10)
            while (x // 10) != 0:
                x = x // 10
                s.append(x % 10)
                i += 1
            for elem in s:
                newx += (elem) * (10 ** i)
                i -= 1
            if oldx < 0:
                newx = -newx
            if ((-2) ** 31) < newx < (2 ** 31 - 1) :
                return newx
            else:
                return 0
        """
        :type x: int
        :rtype: int
        """
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = str(-x)
            x = -int(x[::-1])
        else:
            x = str(x)
            x = int(x[::-1])
        # if x in [-2**31, 2**31-1]:
        if x > 2**31-1 or x < -2**31:
            return 0
        else:
            return x
