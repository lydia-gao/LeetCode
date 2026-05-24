class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def dfs(sum: int, index: int):
            if sum == target:
                # if i pass path in as arg in dfs, do i need to do deepcopy for path here? i think yes, since python pass args by reference
                final = path[:]
                res.append(final)
                return
            if sum > target:
                return
            for i in range(index, len(candidates)):
                curr = sum + candidates[i]
                path.append(candidates[i])
                dfs(curr, i)
                path.pop()
        dfs(0, 0)
        return res
           
