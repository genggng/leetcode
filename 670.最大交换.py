#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start



class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        1. 需要知道最大位的值是x
        2. 如果num[0] == x,需要寻找一个小于x的高位
        3. 找到高位，需要找到一个值为x的最低的位。
        4. 交换
        """
        s = list(str(num))
        n = len(s)
        max_idx = n-1
        idx1,idx2 = -1,-1 #两个需要交换的位置
        for i in range(n-1,-1,-1):
            if s[i] > s[max_idx]:
                max_idx = i  #最大值的索引
            elif s[i] < s[max_idx]:
                idx1,idx2 = i, max_idx  
                #可以交换的序列,会逐渐往前找最高位
                # 注意只在s[i]<s[max_idx]时才会更新，这样即使遇到高位更大值也无所谓
        if idx1 < 0:
            return num
        s[idx1],s[idx2] = s[idx2],s[idx1]
        return int(''.join(s))
# @lc code=end

