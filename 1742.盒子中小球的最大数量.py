#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        """
        模拟法：统计每个小球防止的盒子
        """
        count = {}
        for num in range(lowLimit,highLimit+1):
            num_sum = 0
            while num:
                r = num%10
                num_sum += r
                num = num//10
            if num_sum not in count.keys():
                count[num_sum] = 0
            count[num_sum] += 1
        return max(count.values())
# @lc code=end

print(Solution().countBalls(19,28))