class Solution:
    def maxArea(self, height: List[int]) -> int:
        if height[-1] > height[0]:
            height = height[::-1]
        biggest = 0
        biggest_L = 0
        for L in range(len(height) - 1):
            if height[L] > biggest_L:
                biggest_L = height[L]
            else:
                continue
            for R in range(L+1, len(height)):
                size = min(height[L], height[R]) * (R - L)
                if size > biggest:
                    biggest = size
        return biggest
