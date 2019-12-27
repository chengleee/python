class Solution:
    def twoSum(self,nums,target):
        x = 0
        y = 1
        for i in nums:
            for j in nums[y:]:
                if i + j == target:
                    return (x,y)
                y += 1
            x += 1
            y = x + 1
