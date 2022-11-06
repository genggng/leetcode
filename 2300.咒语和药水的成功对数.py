#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#

# @lc code=start
from audioop import reverse
from bisect import bisect_right


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 超时
        # n = len(spells)
        # res = [0]*n
        # spells = list(zip(spells,list(range(n))))
        # spells.sort(reverse=True)
        # potions.sort(reverse=True)
        # for spell,index in spells:
        #     if spell*potions[0]<success:
        #         break
        #     for potion in potions:
        #         if spell*potion >= success:
        #             res[index] += 1
        #         else:
        #             break
        # return res
        """
        使用二分查找，只要找到临界点，就不用继续找了。
        找到potion*spell >= success   
        potion >= ceil(success / spell)
        potion > up(success-1 / spell)
        """
        res = []
        potions.sort()
        m = len(potions)
        for spell in spells:
            valid_num = m - bisect_right(potions,(success-1)//spell)
            res.append(valid_num)
        return res 
# @lc code=end

