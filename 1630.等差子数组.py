#
# @lc app=leetcode.cn id=1630 lang=python3
#
# [1630] 等差子数组
#

# @lc code=start
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res  = []
        for l_idx,r_idx in zip(l,r):
            sub_nums = nums[l_idx:r_idx+1]
            sub_nums.sort()
            if len(sub_nums) == 2:
                res.append(True)
            else:
                flag = True
                for i in range(len(sub_nums)-2):
                    if sub_nums[i+1] - sub_nums[i] != sub_nums[i+2] - sub_nums[i+1]:
                        flag = False
                        break
                res.append(flag)
        return res
                



# @lc code=end

