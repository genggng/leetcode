#
# @lc app=leetcode.cn id=672 lang=python3
#
# [672] 灯泡开关 Ⅱ
#

# @lc code=start
class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        """
        每个开关，操作两次等于没有操作，因此只用考虑是否操作某个开关即可。
        考虑1： 如何选择4个开关是否操作。
        考虑2：不同的开关操作之间存在交互影响。
            同时操作2,3相当于操作1
            同时操作1,2相当于操作3
            同时操作1,3相当于操作2
            操作4,会和操作2和操作3交互
        更形式化的表述为：
        对于灯的标号
        6k+1  受1,3,4影响
        6k+2,6k+6 受1,2影响
        6k+3,6k+5 受1,3影响
        6k+4   受1,2,4影响
        因此只用考虑[1,2,3,4] 这四个灯泡的状态即可
        """
        seen = set()
        for i in range(2**4): #四个开关的状态,共16种，可以用一个4位的二进制数表示。
            pressArr = [(i>>j)&1 for j in range(4)]  #四个按钮的情况，十进制提取二进制各位,一个pressArr代表一种准备做的按键策略
            if sum(pressArr) %2 == presses %2 and sum(pressArr) <= presses:  #如果预设按钮与真实次数奇偶性相同，并且真实的按键次数足够
                status = pressArr[0] ^ pressArr[1] ^ pressArr[3]  #0号灯的状态
                if n>=2:
                    status |= (pressArr[0] ^ pressArr[1]) << 1  #1号灯的状态
                if n>=3:
                    status |= (pressArr[0] ^ pressArr[2]) << 2  #2号灯状态
                if n>=4:
                    status |= (pressArr[0] ^ pressArr[1]^pressArr[3]) << 3  #3号灯状态
                seen.add(status)
        return len(seen)
# @lc code=end

