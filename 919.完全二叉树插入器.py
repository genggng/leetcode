#
# @lc app=leetcode.cn id=919 lang=python3
#
# [919] 完全二叉树插入器
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:
    """
    给每个节点标号：根节点为1
    对于任意节点x，其左子树节点为2x，右子树节点为2x+1
    """
    def __init__(self, root: TreeNode):
        self.root = root
        self.cnt = 0  #记录节点数据，其实也是最后一个节点的标好。

        q = deque([root]) #获取节点的数目
        while q:
            self.cnt += 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)



    def insert(self, val: int) -> int:
        self.cnt += 1
        child = TreeNode(val)
        node = self.root

        height = self.cnt.bit_length() - 1  #满二叉树高度

        for i in range(height-1,0,-1):
            if self.cnt &(1<<i):  #提取坐标二进制第i位，从高位取
                node = node.right
            else:
                node = node.left
        if self.cnt & 1:
            node.right = child
        else:
            node.left = child

        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
# @lc code=end

