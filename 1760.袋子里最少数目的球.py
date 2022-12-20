#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#

import heapq
from typing import List
import math
# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        理论上最小值为：
        sum(nums) / (len(nums)+maxOperations)
        使用堆来维护数组的最大值,但是会超时
        """
        # h = []
        # if len(nums) == 1:
        #     return math.ceil(nums[0]/(1+maxOperations))

        # for num in nums:
        #     heapq.heappush(h,(-1*num,1)) #最大堆

        # while maxOperations>0:
        #     max_value,cnt = heapq.heappop(h)
        #     second_value,_ = h[0]
        #     new_cnt = max_value // second_value + 1 #超过第二名
        #     max_value = (max_value*cnt)/new_cnt  #
        #     heapq.heappush(h,(max_value,new_cnt))
        #     maxOperations -= (new_cnt-cnt)
        # return math.ceil(-1*h[0][0])

        """
        二分查找，寻找需要能够符合条件的开销y
        计算此时需要的操作次数。
        如果操作次数小于maxop，那么调整在右区间中查找，同时保留当店y为一个答案
        否则就查找左区间。
        """
        left, right, ans = 1, max(nums), 0
        while left <= right:
            y = (left + right) // 2
            ops = sum((x - 1) // y for x in nums)
            if ops <= maxOperations:
                ans = y
                right = y - 1
            else:
                left = y + 1
        
        return ans
# @lc code=end
a1 = [988,289,805,241,930,954,202,399,179,248,651,898,914,656,213,716,44,541,366,963,12,258,631,26,210,286,984,10,585,173,582,700,322,539,181,260,7,265,594,593,56,113,351,363,761,503,504,321,983,253,205,327,869,408,301,1000,608,723,277,240,367,19,15,517,190,782,397,150,9,341,362,359,806,794,741,360,505,506,383,523,951,583,621,828,857,869,251,196,481,675,295,957,844,648,129,455,73,997,458,142,423,668,584,746,284,900,594,635,793,120,477,883,678,683,318,678,762,899,224,506,37,832,467,673,298,60,726,177,39,633,405,156,596,55,226,296,195,944,807,441,545,166,505,665,215,285,772,981,677,112,886,404,913,855,401,641,166,788,827,840,250,894,253,99,448,661,358,975,681,448,868,641,495,87,510,804,651,168,611,422,794,396,311,754,950,156,626,32]

print(Solution().minimumSize(a1,95))
