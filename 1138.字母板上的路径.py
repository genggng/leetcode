#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        """
        返回一条包含target所有字符的最短路径。
        字符表位置是固定的，因此最短路径长度是唯一的，但是路径不唯一。
        """
        board = {
            "a":(0,0),"b":(0,1),"c":(0,2),"d":(0,3),"e":(0,4),
            "f":(1,0),"g":(1,1),"h":(1,2),"i":(1,3),"j":(1,4),
            "k":(2,0),"l":(2,1),"m":(2,2),"n":(2,3),"o":(2,4),
            "p":(3,0),"q":(3,1),"r":(3,2),"s":(3,3),"t":(3,4),
            "u":(4,0),"v":(4,1),"w":(4,2),"x":(4,3),"y":(4,4),
            "z":(5,0)
        }
        pre = (0,0)
        res = []
        for c in target:
            loc = board[c]
            x,y = loc[0]-pre[0],loc[1]-pre[1]
            x_op,y_op = [],[]
            if y>0:
                y_op = ["R"]*y
            if y<0:
                y_op = ["L"]*(-y)
            if x>0:
                x_op = ["D"]*x
            if x<0:
                x_op = ["U"]*(-x)

            if pre == (5,0):
                res += (x_op + y_op)
            else:
                res += (y_op + x_op)
            res.append("!")
            pre = loc
        return "".join(res)

# @lc code=end

