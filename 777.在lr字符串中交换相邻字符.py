#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#

# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L可以借助X往右移动，R可以借助X往左移动。
        # start中L的坐标不能比end中L的坐标小，因为只能向右移动
        # start中R的坐标不能比end中R的坐标大，因为只能向右移动
        i,j,n =0,0,len(start)  #双指针，指向两个字符串
        while i<n or j<n:
            while i<n and start[i] == 'X': i += 1 #跳过X
            while j<n and end[j] == 'X': j += 1
            if i == n or j == n: return i == j
            if start[i] != end[j]: return False #删除X后，两个列表必须相同，即LR相对位置是一样的，因为L和R只能跨过X
            if start[i] == "L" and i<j : return False #L不能左移
            if start[i] == "R" and i>j : return False #R不能右移
            i += 1
            j += 1
        return i == j
 # @lc code=end

