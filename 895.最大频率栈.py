#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  #记录每个元素出现的额频率
        self.group = defaultdict(list)  #记录相同频率下，元素的次序。
        self.max_freq = 0  #元素的最高频率
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.max_freq = max(self.max_freq,self.freq[val])

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if len(self.group[self.max_freq]) == 0:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

