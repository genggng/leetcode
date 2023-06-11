#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.16%)
# Likes:    1359
# Dislikes: 0
# Total Accepted:    525.8K
# Total Submissions: 681.4K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 
# 你可以按 任何顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 示例 2：
# 
# 
# 输入：n = 1, k = 1
# 输出：[[1]]
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return [list(i) for i in combinations(iterable=range(1, n + 1), r=k)]

# @lc code=end

