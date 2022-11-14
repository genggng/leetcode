from typing import List
"""
6240. 树上最大得分和路径 显示英文描述 
题目难度Medium
一个 n 个节点的无向树，节点编号为 0 到 n - 1 ，树的根结点是 0 号节点。给你一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] ，表示节点 ai 和 bi 在树中有一条边。

在每一个节点 i 处有一扇门。同时给你一个都是偶数的数组 amount ，其中 amount[i] 表示：

如果 amount[i] 的值是负数，那么它表示打开节点 i 处门扣除的分数。
如果 amount[i] 的值是正数，那么它表示打开节点 i 处门加上的分数。
游戏按照如下规则进行：

一开始，Alice 在节点 0 处，Bob 在节点 bob 处。
每一秒钟，Alice 和 Bob 分别 移动到相邻的节点。Alice 朝着某个 叶子结点 移动，Bob 朝着节点 0 移动。
对于他们之间路径上的 每一个 节点，Alice 和 Bob 要么打开门并扣分，要么打开门并加分。注意：
如果门 已经打开 （被另一个人打开），不会有额外加分也不会扣分。
如果 Alice 和 Bob 同时 到达一个节点，他们会共享这个节点的加分或者扣分。换言之，如果打开这扇门扣 c 分，那么 Alice 和 Bob 分别扣 c / 2 分。如果这扇门的加分为 c ，那么他们分别加 c / 2 分。
如果 Alice 到达了一个叶子结点，她会停止移动。类似的，如果 Bob 到达了节点 0 ，他也会停止移动。注意这些事件互相 独立 ，不会影响另一方移动。
请你返回 Alice 朝最优叶子结点移动的 最大 净得分。
"""
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        