#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        这一题问的是任意两个区间互不重叠。
        """
        intervals.sort()
        res = 0
        for i in range(1,len(intervals)):
            _,e = intervals[i-1]
            s1,e1 = intervals[i]
            if e>s1: #有重叠
                res += 1 #删除一个
                intervals[i][1] = min(e,e1) #删除end更大的那个
        return res


# @lc code=end

