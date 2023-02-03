#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#

# @lc code=start
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        """
        1. 对于每个用户，记录其操作的时间点，相同的时间点算一个。
        2. 统计每种时间点个数的用户数。
        """
        user_time = {}
        for log in logs:
            id,time = log
            if id not in user_time.keys():
                user_time[id] = set([])
            user_time[id].add(time)
        dist = {}
        for _,op_set in user_time.items():
            minutes = len(op_set)
            if minutes not in dist.keys():
                dist[minutes] = 0
            dist[minutes] += 1
        res = [0]*k
        for k,v in dist.items():
            res[k-1] = v
        return res


# @lc code=end

