#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#
# https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/description/
#
# algorithms
# Medium (61.73%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 39.8K
# Testcase Example:  '["cbd"]\n["zaaaz"]'
#
# 定义一个函数 f(s)，统计 s  中（按字典序比较）最小字母的出现频次 ，其中 s 是一个非空字符串。
# 
# 例如，若 s = "dcce"，那么 f(s) = 2，因为字典序最小字母是 "c"，它出现了 2 次。
# 
# 现在，给你两个字符串数组待查表 queries 和词汇表 words 。对于每次查询 queries[i] ，需统计 words 中满足
# f(queries[i]) < f(W) 的 词的数目 ，W 表示词汇表 words 中的每个词。
# 
# 请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是第 i 次查询的结果。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：queries = ["cbd"], words = ["zaaaz"]
# 输出：[1]
# 解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。
# 
# 
# 示例 2：
# 
# 
# 输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# 输出：[1,2]
# 解释：第一个查询 f("bbb") < f("aaaa")，第二个查询 f("aaa") 和 f("aaaa") 都 > f("cc")。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# queries[i][j]、words[i][j] 都由小写英文字母组成
# 
# 
#

# @lc code=start
from collections import Counter
from typing import List
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # generate every word fuctions values.
        def f(s):
            cnt = Counter(s)
            k = min(cnt.keys())
            return cnt[k]
        w_values = [f(w) for w in words]
        q_values = [(f(q),idx) for idx,q in enumerate(queries)]
        w_values.sort()
        q_values.sort()

        res = [0]*len(q_values)
        j = 0
        # print(q_values,w_values)
        for q,idx in q_values:
            while j < len(w_values):
                if w_values[j]>q:
                    res[idx] = len(w_values) - j
                    break
                j += 1
            
            if j == len(w_values):
                res[idx] = 0
        
        return res
# @lc code=end
queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(Solution().numSmallerByFrequency(queries=queries,words=words))
