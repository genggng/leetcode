from typing import List,Optional

"""
6378. 最小化旅行的价格总和 显示英文描述 
现有一棵无向、无根的树，树中有 n 个节点，按从 0 到 n - 1 编号。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间存在一条边。

每个节点都关联一个价格。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价格。

给定路径的 价格总和 是该路径上所有节点的价格之和。

另给你一个二维整数数组 trips ，其中 trips[i] = [starti, endi] 表示您从节点 starti 开始第 i 次旅行，并通过任何你喜欢的路径前往节点 endi 。

在执行第一次旅行之前，你可以选择一些 非相邻节点 并将价格减半。

返回执行所有旅行的最小价格总和。
"""
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 可以证明，从一个节点到另一个节点的路径只有一条。
        # 计算每个节点需要被访问的次数，得到一个真实cost。
        pass