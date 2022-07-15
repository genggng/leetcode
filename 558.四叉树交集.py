#
# @lc app=leetcode.cn id=558 lang=python3
#
# [558] 四叉树交集
#

# @lc code=start

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

from collections import deque

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        """
        两个四叉树形状相同，只需同时递归遍历他们即可。
        在遍历的过程中，在第一棵树上原地修改。
        最终返回二叉树1即可。
        使用层次遍历，非递归。
        """
        # q1 = deque([quadTree1])
        # q2 = deque([quadTree2])
        # while q1:
        #     node1 = q1.popleft()
        #     node2 = q2.popleft()
        #     if node1:
        #         if node1.isLeaf:
        #             node1.val = node1.val | node2.val
        #         else:
        #             q1.append(node1.topLeft)
        #             q1.append(node1.bottomLeft)
        #             q1.append(node1.bottomRight)
        #             q1.append(node1.topRight)
        #             q2.append(node2.topLeft)
        #             q2.append(node2.bottomLeft)
        #             q2.append(node2.bottomRight)
        #             q2.append(node2.topRight)
        """
        XXXXXXXXX
        上面的思想不对，因为需要对四叉树进行简化。如果一个子树下所有元素都是相同的值。
        这棵子树可以变为叶子节点。
        为了高效，只能使用递归方法。

        """
        def dfs(q1:'Node',q2:'Node'):
            # 返回值代表该节点的val有效，可以设为叶子节点
            if not q1: return True
            if q1.isLeaf:
                q1.val = q1.val | q2.val
                return True

            # 反向修改节点
            if dfs(q1.topLeft,q2.topLeft) and dfs(q1.bottomLeft,q2.bottomLeft) \
             and dfs(q1.bottomRight,q2.bottomRight) and dfs(q1.topRight,q2.topRight):
                ls = [q1.topLeft,q1.bottomLeft,q1.bottomRight,q1.topRight]
                val_count = 0
                null_count = 0
                for node in ls:
                    if node:
                        val_count += node.val
                    else:
                        null_count += 1
                
                # 修改节点属性为叶子节点
                if val_count == 0:
                    q1.isLeaf = True
                    q1.val = 0
                if val_count + null_count == 4:
                    q1.isLeaf = True
                    q1.val = 1
                 
                if q1.isLeaf:   #置空孩子节点
                    q1.topLeft = None
                    q1.bottomLeft = None
                    q1.bottomRight = None
                    q1.topRight = None

            return q1.isLeaf

        # dfs(quadTree1,quadTree2)

        """
        上面的做法也不对，因为两颗矩阵值不同，即使矩阵维数相同，生成四叉树形状也可能不同。
                核心：只有叶子节点的值是有效的。
        不存在空节点，一个节点要么是叶子节点，要么是有四个孩子的节点。
        """
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            # 如果q1是叶子节点，如果q1的值为1，利用的是或运算的性质，直接返回node(1,1)即可
            # 如果q1=0，那么真个区域的节点值由q2确定
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            # 如果q2s是叶子结点，就调转顺序，把q2放前面，使用相同的逻辑。
            return self.intersect(quadTree2, quadTree1)
        # 如果q1和q2都不是叶子节点
        # 那么就递归判断他们的四个孩子区域。
        o1 = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        o2 = self.intersect(quadTree1.topRight, quadTree2.topRight)
        o3 = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        o4 = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        
        # 如果他们的四个孩子都是叶子节点，那么该节点就整体变为叶子节点。
        if o1.isLeaf and o2.isLeaf and o3.isLeaf and o4.isLeaf and o1.val == o2.val == o3.val == o4.val:
            return Node(o1.val, True)
        # 否则就返回有孩子的节点
        return Node(False, False, o1, o2, o3, o4)


# @lc code=end

