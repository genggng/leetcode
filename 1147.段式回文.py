#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0
        i,j = 0,len(text)-1
        # 寻找a[:i+1] 和 a[j:] 相同
        while i<j:
            if text[:i+1] == text[j:]:
                break
            i += 1
            j -= 1
        # print(text[:i+1])
        inc = 2 if i<j else 1
        return inc + self.longestDecomposition(text[i+1:j])

# @lc code=end
text = "ghiabcdefhelloadamhelloabcdefghi"
print(Solution().longestDecomposition(text))
