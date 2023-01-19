#
# @lc app=leetcode.cn id=2299 lang=python3
#
# [2299] 强密码检验器 II
#

# @lc code=start
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        special_char = set(['!','@','#','$','%','^','&','*','(',')','-','+'])
        if len(password)<8:
            return False
        flag = [False]*4 #四个条件
        for i,c in enumerate(password):
            if i>0 and password[i] == password[i-1]:
                return False
            if c.islower():
                flag[0] = True 
            elif c.isupper():
                flag[1] = True
            elif c.isdigit():
                flag[2] = True
            elif c in special_char:
                flag[3] = True
        return all(flag)
# @lc code=end
r = Solution().strongPasswordCheckerII("*Aa1a1a1")
print(r)
