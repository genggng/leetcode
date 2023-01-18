#
# @lc app=leetcode.cn id=1814 lang=python3
#
# [1814] 统计一个数组中好对子的数目
#
from collections import Counter
from scipy.special import comb, perm
from typing import List
# @lc code=start
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        i和j对应的元素，与对方反转后元素相加，和相同
        关键：一个元素反转的差值，能把另一个元素反转弥补。
        计算每一个反转后的差值，与之和为0的元素，即为陪对项目。
        """
        mod = int(1e9+7)
        for i,num in enumerate(nums):
            rev_num = int(str(num)[::-1])
            nums[i] = num - rev_num  #存储和其相同的差值
        res = 0
        num_dict = Counter(nums)
        for key in num_dict.keys():
            res += comb(num_dict[key],2)  #从所有0的位置选出来两个位置
        return res % mod


# @lc code=end
Solution().countNicePairs([42,11,1,97])
