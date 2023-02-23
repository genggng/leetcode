#
# @lc app=leetcode.cn id=1238 lang=python3
#
# [1238] 循环码排列
#

# @lc code=start
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # 生成格雷编码
        res = []
        for i in range(2**n):
            gray_num = (i^(i>>1))
            res.append(start ^ gray_num)
        return res

# @lc code=end

