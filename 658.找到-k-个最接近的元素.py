#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
import math
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        首先二分查找到离x最近的元素
        """
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[len(arr)-k:]

        l,r = 0,len(arr)-1
        m = 0
        while l<=r:
            m = (l+r)//2
            if arr[m] == x:
                break
            if arr[m] > x:
                r = m - 1
            else:
                l = m + 1
        # 此时的m并不一定是最近的，可能前一个或者后一个都比它近
        m_abs = abs(arr[m]-x)
        min_idx = m
        if  m - 1>=0 and abs(arr[m-1]-x) <= m_abs:
            min_idx = m - 1
        if m + 1 <len(arr) and abs(arr[m+1]-x) < m_abs:
            min_idx = m + 1

        # print("min_idx:",min_idx)

        l = min_idx - 1
        r =  min_idx + 1
        k -= 1
        while k>0:
            print(l,r)
            if l <0:
                r += 1
                k -= 1
                continue
            if r>=len(arr):
                l -= 1
                k -= 1
                continue

            l_abs = abs(arr[l] - x)
            r_abs = abs(arr[r] - x)
            # print(f"l_abs:{l_abs} r_abs:{r_abs}")
            if l_abs <= r_abs:
                l -= 1
            else:
                r += 1
            k -= 1
        
        return arr[l+1:r]

# @lc code=end

