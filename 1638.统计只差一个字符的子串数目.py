#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        """
        暴力法,遍历s和t的起始位置
        """
        m,n = len(s),len(t)
        res = 0
        for i in range(m):
            for j in range(n):
                cnt = 0  #不同的次数
                for k in range(min(m-i,n-j)):
                    if s[i+k] == t[j+k]:
                        if cnt == 1:
                            res += 1
                    else:
                        if cnt == 0:
                            cnt = 1
                            res += 1
                        else:  #cnt = 1
                            break
        return res
                        


# @lc code=end

