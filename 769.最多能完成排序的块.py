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
        block_max_value = [arr[0]] #每个块的最大值
        for x in arr[1:]:
            if x > block_max_value[-1]:
                block_max_value.append(x)
            else:
                if len(block_max_value) == 1 or x > block_max_value[-2]:
                    continue
                max_value = block_max_value[-1]
                for i in range(len(block_max_value)):
                    if x < block_max_value[i]:
                        # 后面所有都需要合并
                        block_max_value = block_max_value[:i]
                        block_max_value.append(max_value)
                        break
        return len(block_max_value)

# @lc code=end
print(Solution().maxChunksToSorted([1,2,0,3]))

