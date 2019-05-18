class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We can transform the list into a sorted list by
        # Subtracting each element bu the first element mod
        # a number larger than the range of numbers in the list.
        #
        # Assuming the list is all ints, MAX_INT - MIN_INT + 1 works best.
        # Now we don't actually have to transform the entire list,
        # just transform each number as we search through it.
        # Don't forget to transform the target in the same way

        def transform(num, first_element):
            # One larger than the max int, used for mod function
            max_int_p1 = 2**33
            return (num - first_element) % max_int_p1

        def binary_search(nums, left, right, transformed_target):
            # Regular Binary Search
            if left <= right:
                middle = (left + right) // 2

                transformed_middle_num = transform(nums[middle], nums[0])

                if transformed_middle_num == transformed_target:
                    return middle
                if transformed_middle_num < transformed_target:
                    return binary_search(nums, middle + 1, right, transformed_target)
                else:
                    return binary_search(nums, left, middle - 1, transformed_target)
            else:
                return -1

        # If the list is empty, the target is not in there
        if not nums:
            return -1
        return binary_search(nums, 0, len(nums) - 1, transform(target, nums[0]))
