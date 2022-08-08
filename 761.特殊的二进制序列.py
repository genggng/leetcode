#
# @lc app=leetcode.cn id=761 lang=python3
#
# [761] 特殊的二进制序列
#

# @lc code=start
class Solution:
    """
    特殊序列一定是以1开头，以0结尾。
    可以交换的两个特殊子串，一定不能包含开头的1和结尾的0.
    可以将首位的1和末尾0删除，获取一个子问题。
    """
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s
        
        cnt = left = 0
        subs = list()

        for i, ch in enumerate(s):
            if ch == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left+1:i]) + "0")
                    left = i + 1
        
        subs.sort(reverse=True)
        return "".join(subs)
# @lc code=end

