class Solution:
    def trap(self, height: List[int]) -> int:

        # Easy to read two pass solution, O(n) time, O(n) space
        result = 0
        highest_before = 0
        highest_left = []

        # Record the tallest wall to the left of each tile
        for i, h in enumerate(height):
            highest_left.append(highest_before)
            highest_before = max(h, highest_before)

        # Remember the tallest wall to the right of each tile and calculate the rain.
        highest_before = 0
        for i in reversed(range(len(height))):
            h = height[i]
            result += max(0, min(highest_before - h, highest_left[i] - h))
            highest_before = max(h, highest_before)

        return result
