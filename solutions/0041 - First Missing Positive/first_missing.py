class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # The first loop relocates each num so that nums[n-1] = n
        # numbers larger than the size of nums or non-positve are disregarded

        def place(nums, num):
            if num > len(nums) or num < 1:
                return
            index = num - 1
            old_num = nums[index]
            if old_num == num:
                return
            nums[index] = num
            place(nums, old_num)

        for num in nums:
            place(nums, num)

        # The second loop looks for the first number out of place in my now sorted list.
        for i in range(len(nums)):
            if i != nums[i] - 1:
                return i + 1
        return len(nums) + 1
