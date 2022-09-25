#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        k_sum = [0] * len(code) #sum(code[i:i+k])
        if k == 0: return k_sum
        n = len(code)
        # 只需要计算所有长度为k的列表值即可,一共需要计算n个
        k_pos = abs(k)
        if k_pos == 1: k_sum[:] = code[:]
        else:
            k_sum[0] = sum(code[0:k_pos])
            for i in range(1,n):
                k_sum[i] = k_sum[i-1] - code[i-1] + code[(i+k_pos-1)%n]
        offest = 1 if k>0 else k
        for i in range(n):
            code[i] = k_sum[(i+offest)%n]
        return code


# @lc code=end

