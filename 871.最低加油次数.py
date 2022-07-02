#
# @lc app=leetcode.cn id=871 lang=python3
#
# [871] 最低加油次数
#

# @lc code=start
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        关键思想：先往前走，如果油不够了，反悔倒回去加油。
        如何加油次数最少：因为到达目的地的耗油量是确定的，优先选油量最多的加油站。

        算法：优先队列+贪心算法
        遍历加油站或者目的地，如果能够开车到这个地方汽油还没耗光，就来这个地方。
        同时把这个加油站加入优先队列，我能加油但是没加。
        如果到达不了加油站，需要从能到的加油站里面挑个油量最多的，反悔回去加油。
        重复迭代，知道到达目的地
        """
        n = len(stations)
        cur_fule = startFuel  #行驶过程中汽油量
        visited_stations = [] # 能够反悔回去的加油站的（负）油量，从而用小根堆实现大根堆的效果
        place = 0  #当前的位置
        res = 0

        for i in range(n+1): #走遍所有加油站+最终目的地
            target_station = stations[i][0] if i<n else target   #下个目标的坐标
            cur_fule = cur_fule-(target_station -place)  #到目标需要耗油
            while cur_fule<0 and visited_stations: #到不了，需要加油
                cur_fule -= heappop(visited_stations)
                res += 1  #加油次数增加
            if cur_fule < 0:  #加油站都空了，还是加不满
                return -1  
            if i <n:
                heappush(visited_stations,-stations[i][1])
                place = target_station  #更新当前坐标
        
        return res
                


# @lc code=end

