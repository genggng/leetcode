#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        for num in nums:
            if num<0:
                arr1.append(num*num)
            else:
                arr2.append(num*num)
        m,n = len(arr1),len(arr2)
        i,j = 0,0
        res = []
        arr1 = arr1[::-1]
        while i<m and j<n:
            a1 = arr1[i]
            a2 = arr2[j]
            if a1<=a2:
                res.append(a1)
                i +=1
            else:
                res.append(a2)
                j += 1
        for k in range(i,m):
            res.append(arr1[k])
        
        for k in range(j,n):
            res.append(arr2[k])
        
        return res


# @lc code=end

