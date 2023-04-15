#
# @lc app=leetcode.cn id=1255 lang=python3
#
# [1255] 得分最高的单词集合
#

# @lc code=start
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res, n = 0, len(words)
        cnt = [Counter(w) for w in words]
        h = Counter(letters)
        for i in range(1, 1 << n):
            x = Counter()
            for j in range(n):
                if i >> j & 1: x += cnt[j]
            if all(v <= h[k] for k, v in x.items()):
                res = max(res, sum(v * score[ord(k) - 97] for k, v in x.items()))
        return res


# @lc code=end