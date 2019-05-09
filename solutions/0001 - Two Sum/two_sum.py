class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        li = []
        for i, num in enumerate(nums):
            if num in li:
                return[li.index(num),i]
            else:
                li.append(target - num)
        return [0,0]
