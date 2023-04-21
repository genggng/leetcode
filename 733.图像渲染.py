#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#
# https://leetcode.cn/problems/flood-fill/description/
#
# algorithms
# Easy (58.66%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    157.8K
# Total Submissions: 269.1K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 有一幅以 m x n 的二维整数数组表示的图画 image ，其中 image[i][j] 表示该图画的像素值大小。
# 
# 你也被给予三个整数 sr ,  sc 和 newColor 。你应该从像素 image[sr][sc] 开始对图像进行 上色填充 。
# 
# 为了完成 上色工作 ，从初始像素开始，记录初始坐标的 上下左右四个方向上
# 像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应 四个方向上
# 像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为 newColor 。
# 
# 最后返回 经过上色渲染后的图像 。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: image = [[1,1,1],[1,1,0],[1,0,1]]，sr = 1, sc = 1, newColor = 2
# 输出: [[2,2,2],[2,2,0],[2,0,1]]
# 解析: 在图像的正中间，(坐标(sr,sc)=(1,1)),在路径上所有符合条件的像素点的颜色都被更改成2。
# 注意，右下角的像素没有更改为2，因为它不是在上下左右四个方向上与初始点相连的像素点。
# 
# 
# 示例 2:
# 
# 
# 输入: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# 输出: [[2,2,2],[2,2,2]]
# 
# 
# 
# 
# 提示:
# 
# 
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n
# 
# 
#
from collections import deque

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        m,n = len(image),len(image[0])
        if old_color == color:
            return image
        q = deque([(sr,sc)])
        while q:
            x,y = q.popleft()
            if 0<=x<m and 0<=y<n and image[x][y] == old_color:
                image[x][y] = color
                for new_loc in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    q.append(new_loc)
        
        return image


# @lc code=end

