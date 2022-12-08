#
# @lc app=leetcode.cn id=1812 lang=python3
#
# [1812] 判断国际象棋棋盘中一个格子的颜色
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        坐标从1开始计数，当横纵坐标的奇偶性相同时，为黑色
        当两者奇偶性不同，为白色
        """
        char_map = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8        }
        x,y= coordinates
        x,y = char_map[x],int(y)
        return bool((x+y)%2 == 1)
# @lc code=end

