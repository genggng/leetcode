#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        用栈模拟，只有栈顶为正数，遇到负数这一种情况会相撞
        """
        stack = []        
        for x in asteroids:
            if not stack or not(stack[-1]>0 and x<0):
                stack.append(x)  #栈为空或者可能相撞
            else:   
                while stack and stack[-1]>0 and x<0:  #往右走遇到往左走的
                    if abs(stack[-1]) < abs(x):  #打不过 
                        stack.pop() #反向进攻
                    else:
                        break   #能打过

                if not stack: 
                    stack.append(x)   #敌人全歼，我占据位置
                    continue
                if stack[-1]<0:
                    stack.append(x)
                    continue

                if abs(stack[-1]) == abs(x):
                    stack.pop()  #同归于尽
        return stack
# @lc code=end

