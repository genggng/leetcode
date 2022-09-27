#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        考虑每一位旋转的情况。
        有效情况： 2,5,6,9(改变) 0,1,8(不改变)
        至少要有一位有“改变数字”。
        思路：
        1. 首先统计每一位的有效数字
        2. 计算所有有效组合情况 C1
        3. 计算无改变数字的有效组合情况 C2
        4. 最终结果=C1-C2
        """
        # 排列不出，只能暴力求解
        res = 0
        diff = {"2","5","6","9"}
        valid = {"3","4","7"}
        for x in range(n+1):
            x = str(x)
            valid_flag,diff_flag = True,False
            for c in x:
                if c in diff:
                    diff_flag = True
                if c in valid:
                    valid_flag = False
                    break
            if valid_flag and diff_flag:
                res += 1
        return res
# @lc code=end

