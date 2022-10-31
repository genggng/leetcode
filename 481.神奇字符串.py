#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#

# @lc code=start
class Solution:
    def magicalString(self, n: int) -> int:
        """
        模拟法，生成神奇字符串
        """
        res = [1,2,2] #生成的序列
        i = 2  #记录要生成的源数据
        res_n = 3
        while res_n<n:
            src_data = res[i]  #原数组作为次数
            new_data = res[-1]%2+1 #上一组是1，新组是2；上一组是2，新组是1
            res += [new_data]*src_data
            res_n += src_data
            i += 1
        return res[:n].count(1)

# @lc code=end

