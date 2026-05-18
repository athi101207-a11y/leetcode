class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):

            # if total equals target, add combination
            if total == target:
                result.append(path[:])
                return

            # stop if total exceeds target
            if total > target:
                return

            # try all possible candidates
            for i in range(start, len(candidates)):

                # include current number
                path.append(candidates[i])

                # reuse same number again
                backtrack(i, path, total + candidates[i])

                # remove last number (backtrack)
                path.pop()

        backtrack(0, [], 0)

        return result


# Example Usage
sol = Solution()

print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 8))
print(sol.combinationSum([2], 1))