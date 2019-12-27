class Solution:
    def addTwoNumbers(self, l1, l2):
        i = 0
        l3 = []
        l3.append(0)
        while (i < len(l1)) and ( i< len(l2)):
            if l1[i] + l2[i] >= 10:
                l3[i] += (l1[i] + l2[i]) % 10
                l3.append(1)
            else:
                l3[i] += l1[i] + l2[i]
                l3.append(0)
            i += 1
        if i == len(l1):
            if len(l3) == len(l1):
                l3.extend(l2[i:])
            else:
                l3[i] += l2[i]
                l3.extend(l2[i+1:])
        else:
            if len(l3) == len(l2):
                l3.extend(l1[i:])
            else:
                l3[i] += l1[i]
                l3.extend(l1[i+1:])
        return tuple(l3)
