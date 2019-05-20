class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1
            result = -1
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return -1

        def findmore(nums, firstpos, target):
            left = right = firstpos

            while True:
                if left > 0 and nums[left - 1] == target:
                    left -= 1
                elif right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1
                else:
                    break
            return [left, right]

        firstpos = binary_search(nums, target)

        if firstpos == -1:
            return [-1, -1]

        return findmore(nums, firstpos, target)
