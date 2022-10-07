"""
欢迎各位勇者来到力扣新手村，本次训练内容为「采集果实」。

在新手村中，各位勇者需要采集一些果实来制作药剂。time[i] 表示勇者每次采集 1～limit 颗第 i 种类型的果实需要的时间（即每次最多可以采集 limit 颗果实）。

当前勇者需要完成「采集若干批果实」的任务， fruits[j] = [type, num] 表示第 j 批需要采集 num 颗 type 类型的果实。采集规则如下：

按 fruits 给定的顺序依次采集每一批次
采集完当前批次的果实才能开始采集下一批次
勇者完成当前批次的采集后将清空背包（即多余的果实将清空）
请计算并返回勇者完成采集任务最少需要的时间。

"""
from typing import List
import math
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
        res = 0
        for fruit in fruits:
            type,num = fruit
            time_per = time[type]
            res += math.ceil(num/limit)*time_per
        return res

print(Solution().getMinimumTime([2,3,2],[[0,2],[1,4],[2,1]],3))