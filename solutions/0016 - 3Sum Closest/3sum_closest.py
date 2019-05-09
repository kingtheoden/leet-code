class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[-1]
        for x in range(len(nums) - 2):
            lo, hi = x+1, len(nums) - 1
            while(lo < hi):
                res = nums[x] + nums[lo] + nums[hi]
                if res < target:
                    lo += 1
                else:
                    hi -= 1
                if res == target:
                    return target
                if abs(res - target) < abs(closest - target):
                    closest = res
        return closest

                
