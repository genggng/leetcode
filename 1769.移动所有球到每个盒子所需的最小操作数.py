#
# @lc app=leetcode.cn id=1769 lang=python3
#
# [1769] 移动所有球到每个盒子所需的最小操作数
#

# @lc code=start
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        计算所有非空盒子到该位置盒子的累计值。
        模拟法很容易，时间复杂度为O(n^2)。
        Accepted
        95/95 cases passed (5956 ms)
        Your runtime beats 5.8 % of python3 submissions
        Your memory usage beats 98.55 % of python3 submissions (15 MB)
        """

        # n = len(boxes)
        # ans = [0]*n
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         if boxes[j] == "1":
        #             ans[i] += abs(j-i)
        # return ans
        """
        优化过程，存在重复计算。
        随着box往右移动，累积和增加还是减少，取决于box左边和右边的box数量。
        95/95 cases passed (52 ms)
        Your runtime beats 78.99 % of python3 submissions
        Your memory usage beats 94.2 % of python3 submissions (15.1 MB)
        """
        n = len(boxes)
        ans = [0]*n
        cnt_left,cnt_right = 0,0 #左边和右边小球数量。
        if boxes[0] == "1":
            cnt_left = 1  
        for j in range(1,n):
            if boxes[j] =="1":
                cnt_right += 1
                ans[0] += j
        for i in range(1,n):
            ans[i] = ans[i-1] + (cnt_left - cnt_right)
            if boxes[i] == "1":
                cnt_left += 1
                cnt_right -= 1
        return ans
            


# @lc code=end

