#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # 要求a一定要在b的前面
        n = len(s)
        b_cnt = [0]*n   # [0:i+1]存在多少个b
        a_cnt = [0]*n   # [i:n] 存在多少个a
        for i,c in enumerate(s):
            if c == "b":
                b_cnt[i] = b_cnt[i-1]+1 if i >0 else 1
            else:
                b_cnt[i] = b_cnt[i-1] if i>0 else 0
        for i in range(n-1,-1,-1):
            c = s[i]
            if c == "a":
                a_cnt[i] += a_cnt[i+1]+1 if i<n-1 else 1
            else:
                a_cnt[i] = a_cnt[i+1] if i<n-1 else 0
        ab_cnt = [a+b for a,b in zip(a_cnt,b_cnt)]
        return min(ab_cnt)-1
# @lc code=end
s = "aababbab"
print(Solution().minimumDeletions(s))
