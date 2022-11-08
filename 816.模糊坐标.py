#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
#

# @lc code=start
from typing import List
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]  #去除括号
        # 有s.length-1种划分情况
        """
        1. 如果字符串首位是0，那么只有一种情况，小数点必须在0后。
        2. 如果字符串末位位0，那么只有一种情况，没有小数点。
        3. 如果0在字符串的中间，那么0没有特殊之处，有n-1种选择。
        """
        def get_num_list(num):
            if num[0] == '0' and num[-1] == '0':
                if len(num) == 1:
                    return [num]
                else:
                    return None  #没有合法的数字
            elif num[0] == '0':
                return ['0.'+num[1:]]
            elif num[-1] == '0':
                return [num]
            else:
                return [num] + [num[:i]+'.'+num[i:] for i in range(1,len(num))]
        res = []
        for i in range(1,len(s)): #i时数字1的end
            # s[0:1]and s[1:n] ; s[0:n-1] and s[n-1:n]
            s1 = s[0:i]
            s2 = s[i:]
            num_list1 = get_num_list(s1)
            num_list2 = get_num_list(s2)
            if num_list1 and num_list2:
                for num1 in num_list1:
                    for num2 in num_list2:
                        res.append('('+num1+', '+num2+')')
        return res
            


# @lc code=end
print(Solution().ambiguousCoordinates("(123)"))
