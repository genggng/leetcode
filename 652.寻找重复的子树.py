#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        关键函数：如何判断两棵树是相同的。
        相同的两个子树，一定不是父子的关系，只可能是兄弟关系。
        自己思考的方法，并不能解决遍历问题
        """
        # res = []
        # def isSameTree(a,b):
        #     "判断两棵树是否相同"
        #     if not a and not b: 
        #         return True
        #     if a and b  and a.val == b.val:
        #         return isSameTree(a.left,b.left) and isSameTree(a.right,b.right)
        #     return False
        # aTree = root.left
        # bTree = root.right

        """
        序列化二叉树，将二叉树用一个字符串表示。
        通过比较字符串相同，即可知道是否为重复子树。
        使用哈希表来判断是否唯一，哈希表的key为序列化字符串,哈希表的value为对应子树的root
        可以使用递归的方法来序列化子树，用x（左子树序列化）(右子树序列化)来标记层次关系
        """
        # seen = dict()  #存储序列化子树
        # repeat = set()  #记录最终的结果
        # def dfs(node)->str:
        #     if not node:
        #         return ""
        #     # 在序列化过程中，进行相同子树的比较
        #     # 每次调用都能获得node为根节点的子树的序列化字符串
        #     s = str(node.val) + "(" + dfs(node.left) + ")(" + dfs(node.right) + ")"
        #     if (tree := seen.get(s,None)):
        #         repeat.add(tree)
        #     else:
        #         seen[s] = node
        #     return s
        # dfs(root)
        # return list(repeat)

        """
        但是上述的空间复杂度又很高，可以给每种子树标号，用序号代替序列化key
        用三元组表示一棵子树（根节点值x，左子树序号l，右子树序号r） 用于区分不同的子树
        """
        idx = 0 #全局标记的索引
        seen = dict() #(x,l,r):(node,idx)
        repeat = set()
        def dfs(node)->int:
            if not node:
                return 0  #用零代表空子树
            
            tri = (node.val,dfs(node.left),dfs(node.right))
            if tri in seen:  #存在相同的子树
                tree,index = seen[tri]
                repeat.add(tree)
                return index #子树结构相同，序号就相同
            else:
                nonlocal idx
                idx += 1  #给新子树编号
                seen[tri] = (node,idx)
                return idx
        
        dfs(root)
        return list(repeat)

            

            


        

# @lc code=end

