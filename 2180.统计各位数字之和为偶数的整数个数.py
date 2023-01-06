#
# @lc app=leetcode.cn id=2180 lang=python3
#
# [2180] 统计各位数字之和为偶数的整数个数
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        """
        第2k个数字和第2k+1个数字各位之和的奇偶性一定不同。
        (0,1) (2,3)...(8,9) (10,11)...(98,99) (100,101)...
        这说明各位之和为奇数和偶数是均匀分布的，只不过在一个长度为2小组内，顺序不定。
        """
        if num%2 == 1:  #刚好能形成完整的(num+1)//2个小组
            return (num+1)//2 -1 #（0,1）这个小组不存在，因为0取不到
        else:
            #  前面有num//2个完整小组，只需要判断num是否和为偶数。
            flag = 1 if sum(map(int,list(str(num))))%2 == 0 else 0
            return num//2 + flag -1 
# @lc code=end
print(Solution().countEven(13))
