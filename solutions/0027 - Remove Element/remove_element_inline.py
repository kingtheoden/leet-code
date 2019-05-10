class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':

        if not nums:
            return 0

        newtail = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[newtail] = nums[i]
                newtail += 1

        return newtail
