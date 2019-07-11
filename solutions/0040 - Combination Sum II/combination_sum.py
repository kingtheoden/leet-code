class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def solve(last_index, solution, total):
            if total >= target:
                if total == target:
                    if sorted(solution) not in result:
                        result.append(sorted(solution))
                return

            for i in range(last_index, len(candidates)):
                num = candidates[i]
                new_total = total + num
                new_solution = solution.copy()
                new_solution.append(num)
                solve(i+1, new_solution, new_total)

        solve(0, [], 0)
        return result
