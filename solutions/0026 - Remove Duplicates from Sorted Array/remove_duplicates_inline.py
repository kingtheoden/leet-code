class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # This technique runs backwards through the list
        # So that the loop is unaffected by the shrinking list
        if not nums:
            return 0
        last = nums[-1]
        for x in reversed(range(len(nums) - 1)):
            if nums[x] != last:
                last = nums[x]
            else:
                del nums[x]
        return len(nums)
