#
# @lc app=leetcode.cn id=1441 lang=python3
#
# [1441] 用栈操作构建数组
#
from typing import List
# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        题目一定能保证有结果
        """
        res = []
        mon_list  = [i+1 for i in range(n)]
        i = 0
        for num in target:
            while mon_list[i]!=num and i<len(mon_list):
                res.append("Push")
                res.append("Pop")
                i += 1
            else:
                res.append("Push")
                i += 1
        return res
# @lc code=end
print(Solution().buildArray([1,3],3))
