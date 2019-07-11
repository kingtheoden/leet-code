class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def solve(total, number_tracker, last_index):
            if total >= target:
                if total == target:
                    result.append(number_tracker)
                return
            for index in range(last_index, len(candidates)):
                num = candidates[index]
                new_tracker = number_tracker.copy()
                new_tracker.append(num)
                new_total = total + num
                solve(new_total, new_tracker, index)

        solve(0, [], 0)
        return result
