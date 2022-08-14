#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        score = 0 # 默认分数为将整个字符作为右子串
        for c in s:
            if c == "1":
                score += 1

        if s[0] == "0": 
            score =  score + 1
        else: score = score - 1
        
        max_score = score

        for i in range(1,len(s)-1):
            if s[i] == "0":
                score += 1
            else:
                score -= 1    
            max_score = max(max_score,score)
        
        return max_score

# @lc code=end

