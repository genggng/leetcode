"""
如果一个正方形矩阵满足下述 全部 条件，则称之为一个 X 矩阵 ：

矩阵对角线上的所有元素都 不是 0
矩阵中所有其他元素都是 0
给你一个大小为 n x n 的二维整数数组 grid ，表示一个正方形矩阵。如果 grid 是一个 X 矩阵 ，返回 true ；否则，返回 false 
"""
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        flag = True
        for i in range(n):
            if not flag: break
            for j in range(n):
                if i==j or i==(n-1-j):
                    if grid[i][j] == 0:
                        flag = False
                        print('up',i,j,grid[i][j])
                        break
                else:
                    if grid[i][j] !=0:
                        print('do',i,j,grid[i][j])
                        flag = False
                        break
        return flag
x = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
s = Solution()
print(s.checkXMatrix(x))