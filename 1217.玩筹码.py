#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        考虑筹码所在索引的奇偶性，转移后的成本
        奇->奇：0
        偶->偶：0
        奇->偶：1
        偶->奇：1
        最后要达到的位置，索引的奇偶性是唯一的。
        我们只用统计所有数字的奇偶性，看最终移到奇数还是偶数位成本更小。
        """
        odd,even = 0,0
        for num in position:
            if num&1: #奇数
                odd += 1
            else:
                even += 1
        
        return min(odd,even) #哪个少，就把他转成另一个


# @lc code=end

