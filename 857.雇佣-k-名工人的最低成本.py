#
# @lc app=leetcode.cn id=857 lang=python3
#
# [857] 雇佣 K 名工人的最低成本
#

# @lc code=start
from cProfile import label
from cmath import inf


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        """
        直觉告诉我，应该雇佣单位工作量费用最少的员工。
        但实际上，也要考虑选择工作本身少的员工，减少总工作量。

        res >= total_quality * (w[i]/ q[i])
        最终要支付的费用，只与 性价比最差的员工，以及总的工作量有关。
        因此确定了最差员工 w[k]/q[k] ，剩下k-1个员工只需要权重更小的情况下，总工作量最小即可。
        """
        pairs = sorted(zip(quality,wage),key=lambda x:x[1]/x[0])
        ans = inf
        total_q = 0
        h = []

        for q,w in pairs[:k-1]:
            total_q += q   #权重最低的k-1个员工总工作量
            heappush(h,-q)  # 维护工作量最少的k-1名员工
        for q,w in pairs[k-1:]:  # 选择第k个员工
            total_q += q    
            heappush(h,-q)  #将第k个员工加入
            ans = min(ans,w/q * total_q)
            total_q += heappop(h)  #这里用的最大堆，弹出工作量最大的员工，满足约束2
        # 由于是按照权重遍历的，因此新加入的员工，他的权重一定大于前面员工的权重，满足约束1
        return ans

# @lc code=end

