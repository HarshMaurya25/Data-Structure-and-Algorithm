class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        ans = []
        prev_end = float('-inf')

        for start , end in intervals:
            if start > prev_end:
                ans.append([start, end])
                prev_end = end
            else:
                if prev_end < end:
                    ans[-1][1] = end
                    prev_end = end
        
        return ans