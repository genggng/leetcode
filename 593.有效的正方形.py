#
# @lc app=leetcode.cn id=593 lang=python3
#
# [593] 有效的正方形
#

# @lc code=start
import numpy as np
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        正方形沿着中心旋转90度，旋转后与之前重合。
        使用旋转矩阵将四个坐标旋转，看是否与之前重合。
        """

        cx = p1[0] + p2[0] + p3[0] + p4[0]
        cy = p1[1] + p2[1] + p3[1] + p4[1]  #本来要除以4，这里避免除法，对每个点放大四倍。
        # 将中心点变换为原点。


        node_list = [p1,p2,p3,p4]
        node_set = {(x[0]*4-cx,x[1]*4-cy) for x in node_list} 

        if len(node_set) < 4:
            return False

        for x,y in node_set:
            if (-y,x) not in node_set:
                # print(tuple(flip90_right(node)))
                return False
        
        return True   
        

# @lc code=end

