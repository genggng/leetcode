#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#

# @lc code=start
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        """
        分类讨论：
        1. 当k=1时，经过移动有n-1个字符串，找到最小的即可。
        2. 当k>=2时，原字符串一定能转为升序的字符串。
        """
        if k ==1:
            ans = s
            for _ in range(len(s)-1):
                s = s[1:] + s[0]
                ans = min(ans,s)
            return ans
        
        return "".join(sorted(s))
# @lc code=end

