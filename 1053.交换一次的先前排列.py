#
# @lc app=leetcode.cn id=1053 lang=python3
#
# [1053] 交换一次的先前排列
#

# @lc code=start
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # 高位h和低位l，需要h>l
        # # h要进行尽量小，l要尽量大
        # 高位的地位要尽量低，低位的地位要尽量高
        
        n = len(arr)
        if n == 1:
            return arr
        for i in range(n-1,-1,-1):
            max_right = -1
            max_loc = -1
            for j in range(i+1,n):
                if arr[i] > arr[j]:  #可以交换的值
                    if max_right < arr[j]:
                        max_right = arr[j]
                        max_loc = j
            if max_loc > 0:
                arr[i],arr[max_loc] = arr[max_loc],arr[i]
                return arr
        return arr



# @lc code=end

