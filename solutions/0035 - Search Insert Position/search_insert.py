class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Edge Cases
        if not nums or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        # Otherwise do a normal BST with a modified finish to return the index if not found.
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        # middle will be on the index closest to the target.
        # Since the interger division always rounds down,
        # our desired result is either replacing the current index
        # or the one in front of it.
        return middle if nums[middle] > target else middle + 1
