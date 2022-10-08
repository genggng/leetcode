#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#

from typing import List
# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2  = [(num,i) for i,num in enumerate(nums2)] #给nums2添加索引
        nums2 = sorted(nums2,key=lambda x:x[0]) # nums2升序
        nums1 = sorted(nums1)  #nums1升序
        res = [0]*len(nums1)
        no_useful_num = []  #没用的数据，插在最后
        j = 0
        i = 0
        while i < len(nums2):
            #为nums每个元素寻找合适的大于的数
            while j<len(nums1):
                num,index = nums2[i]
                if nums1[j] > num: #找到合适的值
                    res[index] = nums1[j]
                    j += 1
                    i += 1
                    break
                else:
                    no_useful_num.append(nums1[j])
                    j += 1
            if j>=len(nums1):
                for k in range(len(no_useful_num)):
                    res[nums2[i+k][1]] = no_useful_num[k]
                return res
        return res
# @lc code=end

print(Solution().advantageCount([0],[0]))
