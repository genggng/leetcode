#
# @lc app=leetcode.cn id=891 lang=python3
#
# [891] 子序列宽度之和
#

# @lc code=start
MOD = int(1e9+7)
pow2 = [1]  #打表，快速计算2**i
for i in range(10**5 + 10):
    pow2.append(pow2[-1]*2 %MOD)
class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        """
        nums长度为n，那么子序列个数有：
        C(n,1) + C(n,2) + ... + C(n,n) = 2^n - 1
        那么每种情况宽度如何计算呢？
        换个思路：
        nums的顺序与最终结果无关，因此将nums从小到大排序
        计算每个数在所有子序列中，当了多少次“大哥”和“小弟”
        当大哥时，是最为子序列的最大值，对最终求和起"正贡献"
        当小弟时，在所在子序列的最小值，对最终求和起"负贡献"
        68/68 cases passed (244 ms)
        Your runtime beats 93.48 % of python3 submissions
        Your memory usage beats 29.35 % of python3 submissions (27.6 MB)
        """
        res = 0
        nums.sort()
        n = len(nums)
        for i in range(n):
            """
            对于元素i
            当大哥的次数为2**i次，i代表大哥前面存在的元素数。
            当小弟的次数为2**(n-i-1)次，n-i-1代表小弟前面存在的元素数。
            """
            res  = (res + nums[i]*(pow2[i] - pow2[n-i-1])+MOD) % MOD  
        return res
# @lc code=end

