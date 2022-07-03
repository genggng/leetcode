#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        首先对数组升序排列
        对于某个元素arr[i]，能与其组成最小对只有arr[i-1],arr[i+1]
        遍历每个对(arr[i],arr[i+1])
        """
        arr.sort()
        res = []
        min_dff = float("inf")
    
        for i in range(len(arr)-1):
            # print(i,len(arr))
            dff = arr[i+1] - arr[i]
            if dff == min_dff:
                res.append([arr[i],arr[i+1]])
            if dff < min_dff:
                min_dff = dff
                res = [[arr[i],arr[i+1]]]
        return res
# @lc code=end

