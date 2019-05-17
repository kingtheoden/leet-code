class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, left, right):
            while left < right:
                swap(nums, left, right)
                left += 1
                right -= 1
            return

        def swap(nums, left, right):
            nums[left], nums[right] = nums[right], nums[left]
            return

        def find_smallest(nums, i):
            smallest = None
            j = i
            for x in range(i+1, len(nums)):
                if nums[x] > nums[i] and (not smallest or nums[x] <= smallest):
                    smallest = nums[x]
                    j = x
            return j

        def helper(nums, i):
            j = find_smallest(nums, i)
            print("j", j)
            swap(nums, i, j)
            reverse(nums, i+1, len(nums) - 1)
            return

        last = None
        for i in reversed(range(len(nums))):
            print(i)
            if last and nums[i] < last:
                print("i", i)
                helper(nums, i)
                return
            last = nums[i]
        reverse(nums, 0, len(nums) - 1)
        return
