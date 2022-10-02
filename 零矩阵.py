# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 找到所有值为0的坐标。
        m = len(matrix)
        n = len(matrix[0])
        x_ax = [0]*m
        y_ax = [0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x_ax[i] = 1
                    y_ax[j] = 1
        for i in range(m):
            for j in range(n):
                if x_ax[i] == 1 or y_ax[j] == 1:
                    matrix[i][j] = 0
        