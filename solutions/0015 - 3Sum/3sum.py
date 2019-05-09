class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for x in range(len(nums) - 2):
            if x == 0 or nums[x] != nums[x-1]:
                lo, hi, res = x+1, len(nums) -1, 0 - nums[x]
                while lo < hi:
                    if nums[lo] + nums[hi] == res:
                        result.append([nums[x], nums[lo], nums[hi]])
                        while (lo < hi and nums[lo] == nums[lo+1]): lo += 1
                        while (lo < hi and nums[hi] == nums[hi-1]): hi -= 1
                        lo += 1
                        hi -= 1
                    elif (nums[lo] + nums[hi] < res):
                        while (lo < hi and nums[lo] == nums[lo+1]): lo += 1
                        lo += 1
                    else:
                        while(lo < hi and nums[hi] == nums[hi-1]): hi -= 1
                        hi -= 1
        return result

        
