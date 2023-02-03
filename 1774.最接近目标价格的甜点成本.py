#
# @lc app=leetcode.cn id=1774 lang=python3
#
# [1774] 最接近目标价格的甜点成本
#

# @lc code=start
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts:List[int], target: int) -> int:
        # res = [float("inf"),-1] #最佳的差值以及对应的价格
        # n = len(baseCosts)
        # m = len(toppingCosts)
        # def dfs(i,r_list,cur_price):
        #     # 深度优先搜索，使用第i种配料和价格。
        #     # r_list记录第i种配料剩余的容量
        #     if i >= 0:
        #         cur_price += toppingCosts[i]
        #         r_list[i] -= 1
        #     diff = abs(cur_price - target)
        #     if cur_price > target and diff >= res[0]:
        #         # 剪枝
        #         return False
        #     if cur_price == target:
        #         return True #误差为0，终止递归
        #     if diff < res[0] or (diff == res[0] and cur_price<res[1]):
        #         res[0] = diff
        #         res[1] = cur_price
            
        #     for i in range(m):
        #         if r_list[i] > 0:
        #             # 还有存货
        #             if dfs(i,r_list,cur_price):
        #                 return True
        #             r_list[i] += 1 #回溯
        # for i in range(n):
        #     cur_price = baseCosts[i]
        #     r_list = [2 for _ in range(m)]
        #     if dfs(-1,r_list,cur_price):
        #         return target
        # return res[1]
        """
        Time Limit Exceeded
        32/89 cases passed (N/A)
        """ 
        x = min(baseCosts)
        if x > target:
            return x
        can = [False] * (target + 1)
        ans = 2 * target - x
        for c in baseCosts:
            if c <= target:
                can[c] = True
            else:
                ans = min(ans, c)
        for c in toppingCosts:
            for count in range(2):
                for i in range(target, 0, -1):
                    if can[i] and i + c > target:
                        ans = min(ans, i + c)
                    if i - c > 0 and not can[i]:
                        can[i] = can[i - c]
        for i in range(ans - target + 1):
            if can[target - i]:
                return target - i
        return ans


# @lc code=end

