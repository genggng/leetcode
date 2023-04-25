#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
class Twitter:

    def __init__(self):
        self.twitter_log = [] # 按照时间顺序，存储twitter
        self.follow_list = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twitter_log.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        cnt = 0
        res = []
        if userId not in self.follow_list:
            self.follow_list[userId] = set()
            self.follow_list[userId].add(userId)

        follers = self.follow_list[userId]
        for id,tw in self.twitter_log[::-1]:
            if id in follers:
                res.append(tw)
                cnt += 1
            if cnt  == 10:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_list:
            self.follow_list[followerId] = set()
            self.follow_list[followerId].add(followerId)

        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_list and followeeId in self.follow_list[followerId]:
            self.follow_list[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

