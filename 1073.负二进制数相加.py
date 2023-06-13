#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
# https://leetcode.cn/problems/adding-two-negabinary-numbers/description/
#
# algorithms
# Medium (35.47%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 15.8K
# Testcase Example:  '[1,1,1,1,1]\n[1,0,1]'
#
# 给出基数为 -2 的两个数 arr1 和 arr2，返回两数相加的结果。
# 
# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1,1,0,1] 表示数字 (-2)^3 +
# (-2)^2 + (-2)^0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。
# 
# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# 输出：[1,0,0,0,0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。
# 
# 
# 
# 
# 示例 2：
# 
# 
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]
# 
# 
# 示例 3：
# 
# 
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 
# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] 和 arr2[i] 都是 0 或 1
# arr1 和 arr2 都没有前导0
# 
# 
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # 转换为10进制
        n1,n2 = len(arr1),len(arr2)

        num = 0
        for i in range(n1):
            num += arr1[i] * (-2) ** (n1-1-i)
        for i in range(n2):
            num += arr2[i] * (-2) ** (n2-1-i)
        
        res = []
        while num:
            r = num %(-2)
            res.append(-r)
            num = (num+r) // (-2)
        
        return res[::-1] if res else [0]

# @lc code=end

