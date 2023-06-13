#
# @lc app=leetcode.cn id=1054 lang=python3
#
# [1054] 距离相等的条形码
#
# https://leetcode.cn/problems/distant-barcodes/description/
#
# algorithms
# Medium (44.77%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 54.3K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
# 
# 请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：barcodes = [1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
# 
# 
# 示例 2：
# 
# 
# 输入：barcodes = [1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
# 
# 
# 
# 提示：
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        q = []
        for x, cx in count.items():
            heapq.heappush(q, (-cx, x))
        res = []
        while len(q) > 0:
            cx, x = heapq.heappop(q)
            if len(res) == 0 or res[-1] != x:
                res.append(x)
                if cx < -1:
                    heapq.heappush(q, (cx + 1, x))
            else:
                cy, y = heapq.heappop(q)
                res.append(y)
                if cy < -1:
                    heapq.heappush(q, (cy + 1, y))
                heapq.heappush(q, (cx, x))
        return res


# @lc code=end
print(Solution().rearrangeBarcodes([1,1,1,1,2,2,3,3]))

