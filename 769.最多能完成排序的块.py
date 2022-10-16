#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#
from typing import List
# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        归并排序的思想。能够分块的条件：
        块1的最大值要小于块2的最小值
        """
        # block_max_value = [arr[0]] #每个块的最大值
        # for x in arr[1:]:
        #     if x > block_max_value[-1]:
        #         block_max_value.append(x)
        #     else:
        #         if len(block_max_value) == 1 or x > block_max_value[-2]:
        #             continue
        #         max_value = block_max_value[-1]
        #         for i in range(len(block_max_value)):
        #             if x < block_max_value[i]:
        #                 # 后面所有都需要合并
        #                 block_max_value = block_max_value[:i]
        #                 block_max_value.append(max_value)
        #                 break
        # return len(block_max_value)
        """
        贪心算法
        这一题有个要点是，每个元素都不相同，相当于是一个排列。
        关键：如果[a0,a1] [a1,a2] [a2,a3]是一个我们需要的分割（分别排序后与是升序）
        那么 [a0,a1] [a0,a2] [a0,a3] 分别排序也和原数组顺序相同（子数组）。
        这一题就可以简化为，在[a0,ai]这个数组，是否为一个[0-i]的一个排列
        要保证这一点，只需要保证max([a0,ai])==i(因为每个元素都不相同)
        """
        res =nmx =  0
        for i,x in enumerate(arr):
            nmx = max(nmx,x)
            res += (nmx == i)
        return res
# @lc code=end
print(Solution().maxChunksToSorted([1,2,0,3]))

