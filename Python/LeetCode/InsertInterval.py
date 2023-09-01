class Solution:
    def insert(self, intervals, newInterval):

        if len(intervals) == 0:
            return [newInterval]

        l = 0
        while (newInterval[0] >= intervals[l][0]):
            l += 1
            if (l == len(intervals)):
                break

        r = len(intervals) - 1
        while (newInterval[1] <= intervals[r][1]):
            r -= 1
            if (r == -1):
                break
        
        l -= 1
        r += 1


        for i in range (l+1, r):
            del intervals[l+1]
            r -= 1

        print(l,r)
        if r == len(intervals) and l == -1:
            return [newInterval]
        
        elif r == len(intervals) and l > -1:   
            if newInterval[0] > intervals[l][1]:
                intervals.insert(r, newInterval)
            else:
                newInterval = [intervals[l][0], newInterval[1]]
                del intervals[l]
                intervals.insert(l, newInterval)
        elif r < len(intervals) and l == -1:  
            if newInterval[1] < intervals[r][0]:
                intervals.insert(r, newInterval)
            else:
                newInterval = [newInterval[0], intervals[r][1]]
                del intervals[r]
                intervals.insert(r, newInterval)
        else:

            if newInterval [0] > intervals[l][1] and newInterval [1] < intervals[r][0]:
                intervals.insert(r, newInterval)
            elif newInterval [0] <= intervals[l][1] and newInterval [1] < intervals[r][0]:
                newInterval = [intervals[l][0], newInterval[1]]
                del intervals[l]
                intervals.insert(r-1, newInterval)
            elif newInterval [0] > intervals[l][1] and newInterval [1] >= intervals[r][0]:
                newInterval = [newInterval[0], intervals[r][1]]
                del intervals[r]
                intervals.insert(r, newInterval)
            elif newInterval [0] <= intervals[l][1] and newInterval [1] >= intervals[r][0]:
                newInterval = [intervals[l][0], intervals[r][1]]
                if (r != l):
                    del intervals[r]
                    del intervals[l]
                else:
                    del intervals[r]
                intervals.insert(l, newInterval)
        

        return intervals
    
# print(Solution().insert([[1,2], [3,4], [5,6], [9,10], [11,15]], [7,8]))
# print(Solution().insert([[1,2], [3,4], [5,6], [9,10], [11,15]], [6,8]))
# print(Solution().insert([[1,2], [3,4], [5,6], [9,10], [11,15]], [7,9]))
# print(Solution().insert([[1,2], [3,4], [5,6], [9,10], [11,15]], [6,9]))
print(Solution().insert([[1,5],[9,12]], [0,4]))
