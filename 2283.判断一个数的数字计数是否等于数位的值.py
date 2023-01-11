#
# @lc app=leetcode.cn id=2283 lang=python3
#
# [2283] 判断一个数的数字计数是否等于数位的值
#
from collections import Counter
# @lc code=start
class Solution:
    def digitCount(self, num: str) -> bool:
        target_dict = Counter(num)
        target_list = ['0']*len(num)
        for key,value in target_dict.items():
            if int(key) >= len(num):
                return False
            target_list[int(key)] = str(value)
        return bool("".join(target_list) == num)

# @lc code=end
Solution().digitCount("030")
