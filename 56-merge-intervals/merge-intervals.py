class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:

            if not result or result[-1][1] < interval[0]:
                result.append(interval)

            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result


intervals = [[1,3],[2,6],[8,10],[15,18]]

obj = Solution()

print(obj.merge(intervals))