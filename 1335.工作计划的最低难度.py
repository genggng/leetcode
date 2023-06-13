#
# @lc app=leetcode.cn id=1335 lang=python3
#
# [1335] 工作计划的最低难度
#
# https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/description/
#
# algorithms
# Hard (60.36%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 11.9K
# Testcase Example:  '[6,5,4,3,2,1]\n2'
#
# 你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。
# 
# 你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。
# 
# 给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是
# jobDifficulty[i]。
# 
# 返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：jobDifficulty = [6,5,4,3,2,1], d = 2
# 输出：7
# 解释：第一天，您可以完成前 5 项工作，总难度 = 6.
# 第二天，您可以完成最后一项工作，总难度 = 1.
# 计划表的难度 = 6 + 1 = 7 
# 
# 
# 示例 2：
# 
# 输入：jobDifficulty = [9,9,9], d = 4
# 输出：-1
# 解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。
# 
# 
# 示例 3：
# 
# 输入：jobDifficulty = [1,1,1], d = 3
# 输出：3
# 解释：工作计划为每天一项工作，总难度为 3 。
# 
# 
# 示例 4：
# 
# 输入：jobDifficulty = [7,1,7,1,7,1], d = 3
# 输出：15
# 
# 
# 示例 5：
# 
# 输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
# 输出：843
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10
# 
# 
#

# @lc code=start
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # 动态规划
        # 最小难度
        # 首先统计每个区间的最大难度
        n = len(jobDifficulty)
        if d > n:
            return -1
        pre = [[0] * n for i in range(n)]
        for i in range(n):
            t = 0
            for j in range(i, n):
                t = max(t, jobDifficulty[j])
                pre[i][j] = t 
        @cache
        def dfs(i, k):
            """
            i: 第i个任务
            k: 第k天
            """
            if k == 0:
                if i == n:
                    return 0
                if i < n:
                    return inf 
            res = inf
            for j in range(i, n):
                res = min(res, dfs(j+1, k-1) + pre[i][j])
            return res 


        return dfs(0, d)

# @lc code=end

