#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
from collections import deque
from typing import List
# @lc code=start
class    Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        岛不一定是实芯的，只要相连即可。
        找到两个岛的最短距离。
        分成两步，先使用dfs或者bfs找到一个岛的所有元素，并将其都设置为-1。
        然后使用bfs，将所有的元素向外扩散一步，直到遇到另一个岛的元素（1），所使用的步数就是最短距离。
        """
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] != 1:
                    continue
                is_land = []  #存储第一个岛的元素坐标
                grid[i][j] = -1  #登陆到第一个岛
                q = deque([(i,j)])  #多源bfs，以node为起始源
                while q:
                    x,y = q.popleft()
                    is_land.append((x,y))  #添加到第一个岛
                    for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = -1  #找到新的元素
                            q.append((nx,ny)) 
                
                # 找到了第一个岛的所有元素，将所有元素置为-1，并且将元素坐标存在island
                q = is_land
                step = 0
                while True:
                    tmp = q #为什么需要tmp，因为需要把q中元素都遍历光，step+1，表示所有元素走一步。
                    q = []
                    for x,y in tmp:
                        for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    return step   #找到另一个岛，结束
                                if grid[nx][ny] == 0:  #找到一个未扩散到的海域
                                    grid[nx][ny] = -1  #标记已扩散到
                                    q.append((nx,ny))  #从新的节点扩散
                    step += 1
            

# @lc code=end
a = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(Solution().shortestBridge(a))
