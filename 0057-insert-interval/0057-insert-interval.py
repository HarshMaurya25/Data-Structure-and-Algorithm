class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = []
        idx = 0

        for start , end in intervals:
            if end >= newInterval[0]:
                break
            else:
                idx += 1
                ans.append([start, end])
        
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(intervals[idx][0],newInterval[0])
            newInterval[1] = max(intervals[idx][1],newInterval[1])
            idx += 1
        
        ans.append(newInterval)

        while idx < len(intervals):
            ans.append(intervals[idx])
            idx += 1
        
        return ans
        