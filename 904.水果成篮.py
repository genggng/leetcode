#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
from typing import List
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        要求：
        1. 必须连续采摘
        2. 可以选择起始树的位置
        等价于：
        求最多包含两种元素的最长子串
        方法：
        双指针法
        """
        i,j,n = 0,0,len(fruits)
        fruits_type = set()
        fruits_num = {}
        res = 0
        while j<n:
            while j < n and len(fruits_type)<=2:
                x = fruits[j]
                fruits_type.add(x)
                if x not in fruits_num.keys():
                    fruits_num[x] = 0
                fruits_num[x] += 1
                j += 1
            if len(fruits_type)<=2:
                res = max(res,j-i)
            else:
                res = max(res,j-i-1)

            while len(fruits_type)>2 and i<j:# 需要将元素删干净
                x = fruits[i]
                fruits_num[x] -= 1
                if fruits_num[x] <= 0:
                    fruits_type.remove(x)
                i += 1
        return res

# @lc code=end
print(Solution().totalFruit([0,1,2]))

