from typing import List
import numpy as np

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        
        def bfs(start,mat):
            m = len(mat)
            n = len(mat[0])
            q = [start]
            res = 0

            while q:
                tmp = []
                for x,y in q:
                    cur_val = mat[x][y]
                    new_loc = [(x,j) for j in range(n)]
                    new_loc += [(i,y) for i in range(m)]
                    for i,j in new_loc:
                        if not(x==i and y==j) and mat[i][j]>cur_val:
                            tmp.append((i,j))
                res += 1
                q = tmp
            return res

        max_step = 0
        m = len(mat)
        n = len(mat[0])
        if m == 1:
            return len(set(mat[0]))
        if n == 1:
            return len(set([mat[i][0] for i in range(m)]))
        
        s = []
        for i in range(m):
            for j in range(n):
                s.append((mat[i][j],i,j))
        s.sort(reverse=True)
        s_dict = {}
        for idx,item in enumerate(s):
            val,i,j = item
            s_dict[(i,j)] = idx

        skip = 0
        print(s)
        for i in range(m):
            for j in range(n):
                print(s_dict[(i,j)],max_step)
                if s_dict[(i,j)] < max_step:
                    skip += 1
                    continue
                    
                max_step = max(max_step,bfs((i,j),mat))
        print(skip)
        return max_step

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        p = []
        for i in range(n):
            for j in range(m):
                p.append((mat[i][j], i, j))
        p = sorted(p)
        l, r = 0, 0
        x, y = [0] * n, [0] * m
        f = [1] * (n * m)
        while l < len(p):
            while r < len(p) and p[r][0] == p[l][0]:
                r += 1
            for i in range(l, r):
                f[i] += max(x[p[i][1]], y[p[i][2]])
            for i in range(l, r):
                x[p[i][1]] = max(f[i], x[p[i][1]])
                y[p[i][2]] = max(f[i], y[p[i][2]])
            l = r
        return max(max(x), max(y))
    
mat = [[-48,-9,5,34,-30,-3,3,-37,21,36,48,38,-30,32,36,45,10,-13,-3],[23,7,-24,-43,-5,-50,-34,3,19,-18,-8,5,-6,-33,2,-42,-50,33,45],[-22,28,-32,-1,1,-22,42,-1,17,34,-25,-32,30,-25,-23,-8,-48,-37,31]]
# print(len(mat[0]))
print(Solution().maxIncreasingCells(mat))