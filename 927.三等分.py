#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#

# @lc code=start
from ctypes import string_at
from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        """
        最naive的想法，遍历所有的双划分。
        保证各部分去掉前导0的情况下，二进制和长度相同
        要点：如果存在的话，子二进制串的首位必是1，末尾是能确定的。
        没有优化，在111个案例超时
        """
        # if 1 in arr:
        #     i = arr.index(1)  #找到起始位置
        # else:
        #     return [0,len(arr)-1]
        
        # arr = list(map(str,arr))

        # j = len(arr) - 1

        # end = arr[-1]
        # while i+1 < j:
        #     # 确保end符合标准
        #     while i+1<j and arr[i] != end:
        #         i += 1
        #     while i+1<j and arr[j-1] != end:
        #         j -= 1

        #     if i+1 >= j:
        #         return [-1,-1]

        #     num1 = int("".join(arr[:i+1]),2)
        #     num2 = int("".join(arr[i+1:j]),2)
        #     num3 = int("".join(arr[j:]),2)
        #     if num1 > num2 or num3 > num2:
        #         return [-1,-1]

        #     if num1 == num2 == num3:
        #         return [i,j]

        #     if num1 < num3:
        #         i += 1
        #     else:
        #         j -= 1


        # return [-1,-1]
            
        # 每一部分1的数量应该相同
        count = arr.count(1)
        if count % 3 :
            return [-1,-1]
        if count == 0:
            return [0,2]
        
        num_one = count //3
        #使用每部分1的数量，能够确定出i
        cur = 0
        start,mid,end = 0,0,0
        # 确定三个1起始坐标
        for i,x in enumerate(arr):
            if x:
                if cur == 0:
                    start = i
                if cur == num_one:
                    mid = i
                if cur == num_one*2:
                    end = i
                cur += 1
        
        valid_len = len(arr) - end  #因为第三段的结尾是确定的
        if start + valid_len <= mid and mid+valid_len <= end: #确保在三部分内
            # 比较三者三段是否相等
            for k in range(valid_len):
                if arr[start+k] != arr[mid+k] or arr[mid+k] != arr[end+k]:
                    return [-1,-1]
            return [start+valid_len-1,mid+valid_len]
            
        return [-1,-1]


        
        

# @lc code=end
print(Solution().threeEqualParts([1,1,1,1,1,1,0,1,1,1]))

