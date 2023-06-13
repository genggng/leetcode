from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        # 暴力法
        m = len(grid)
        n = len(grid[0])
        answer = [[0]*n for _ in range(m)]

        # 总共有m+n个对角线
        # 每个对角线上元素，横纵坐标递增
        starts = [(i,0) for i in range(m)]
        starts += [(0,j) for j in range(1,n)]
        for start in starts:
            line = [start]
            i,j = start
            while True:
                i += 1
                j += 1
                if i<m and j<n:
                    line.append((i,j))
                else:
                    break
            line_val = [grid[i][j] for i,j in line]
            for k in range(len(line_val)):
                i,j = line[k]
                left = len(set(line_val[:k]))
                right = len(set(line_val[k+1:]))
                answer[i][j] = abs(left-right)
            
        return answer

                