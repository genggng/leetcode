"""
6392. 使数组所有元素变成 1 的最少操作次数 显示英文描述 
给你一个下标从 0 开始的 正 整数数组 nums 。你可以对数组执行以下操作 任意 次：

选择一个满足 0 <= i < n - 1 的下标 i ，将 nums[i] 或者 nums[i+1] 两者之一替换成它们的最大公约数。
请你返回使数组 nums 中所有元素都等于 1 的 最少 操作次数。如果无法让数组全部变成 1 ，请你返回 -1 。

两个正整数的最大公约数指的是能整除这两个数的最大正整数。

 

示例 1：

输入：nums = [2,6,3,4]
输出：4
解释：我们可以执行以下操作：
- 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。
- 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。
- 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。
- 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
示例 2：

输入：nums = [2,10,6,14]
输出：-1
解释：无法将所有元素都变成 1 。
 

提示：

2 <= nums.length <= 50
1 <= nums[i] <= 106
"""
from typing import List
from math import gcd
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 寻找两个互质的因子,只要出现一个1，就能完成任务
        # 但是一对非互质的，也可以变出互质的。
        flag = False
        need = 0
        min_op = 10e9
        for l in range(len(nums)-1):
            for k in range(1,len(nums)-l):
                # print(nums[l:l+k+1])
                g = gcd(*nums[l:l+k+1])
                if g == 1:
                    flag = True
                    min_op = min(k-1,min_op)
                    continue
        if not flag:
            return -1
        
        for num in nums:
            if num != 1:
                need += 1


        return need+min_op
nums = [846237,105643,71480,567494,315367,503911,836510,984966,748650]
# nums = [6,10,15]
print(Solution().minOperations(nums))    
