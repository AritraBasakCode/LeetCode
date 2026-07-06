class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #Sorting the Intervals then Comparing
        intervals.sort(key=lambda x: (x[0], -x[1]))
        valid_intervals = 0
        maxEnd = -1

        for start, end in intervals:
            if end > maxEnd:
                valid_intervals += 1
                maxEnd = end
        
        return valid_intervals