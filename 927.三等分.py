#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#

# @lc code=start
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
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        s = sum(arr)
        if s % 3:
            return [-1, -1]
        if s == 0:
            return [0, 2]

        partial = s // 3
        first = second = third = cur = 0
        for i, x in enumerate(arr):
            if x:
                if cur == 0:
                    first = i
                elif cur == partial:
                    second = i
                elif cur == 2 * partial:
                    third = i
                cur += 1

        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]        
        

# @lc code=end
print(Solution().threeEqualParts([1,1,1,1,1,1,0,1,1,1]))

