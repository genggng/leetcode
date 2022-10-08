#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#

# @lc code=start


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        exist_flag = False  #是否存在1
        end_flag = False  #是否在存在1的情况下遇到0
        for c in s:
            if c == '1':
                if end_flag:
                    return False
                exist_flag = True
            else:
                if exist_flag:
                    end_flag = True
 
        return True


# @lc code=end

