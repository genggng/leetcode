#
# @lc app=leetcode.cn id=1797 lang=python3
#
# [1797] 设计一个验证系统
#

# @lc code=start
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.usr_list = {}  #维护每个tokenid的上次申请时刻
        self.live_time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.usr_list[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.usr_list.keys() and self.usr_list[tokenId] + self.live_time > currentTime: 
            self.usr_list[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for time in self.usr_list.values():
            if time +self.live_time > currentTime:
                res += 1
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
# @lc code=end

