#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 要想没有环，需要在一个循环中方向不变
        # 同时保证最后没有回到原点
        loc = (0,0)
        cnt = 0
        direct = [(0,1),(1,0),(0,-1),(-1,0)]
        start = 0

        for c in instructions:
            
            if c == "G":
                inc = direct[start%4]
                loc = (loc[0]+inc[0],loc[1]+inc[1])
            if c == "L":
                cnt += 1
                start += 1
            if c == "R":
                cnt -= 1
                start -= 1
        # print(loc) 
        if loc != (0,0) and cnt%4 == 0:
            return False
        else:
            return True

# @lc code=end
x  = "GLRLLGLL" 
print(Solution().isRobotBounded(x))

