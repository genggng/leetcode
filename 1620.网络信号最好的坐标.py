#
# @lc app=leetcode.cn id=1620 lang=python3
#
# [1620] 网络信号最好的坐标
#

# @lc code=start
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def get_strength(x,y):
            strength = 0
            for tow_x,tow_y,q in towers:
                d = ((tow_x-x)**2 + (tow_y-y)**2)**0.5
                strength += 0 if d > radius else int(q/(1+d))
            return strength
        
        """
        暴力法：计算每个坐标到的信号强度。
        """
        x_max = max([x[0] for x in towers])
        y_max = max([x[1] for x in towers])
        res = None
        max_strength = -1
        for i in range(x_max+1):
            for j in range(y_max+1):
                stg = get_strength(i,j)
                if stg > max_strength:
                    max_strength = stg
                    res = [i,j]
        return res


# @lc code=end

