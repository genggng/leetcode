"""
6202. 使用机器人打印字典序最小的字符串 显示英文描述 
给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：

删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
请你返回纸上能写出的字典序最小的字符串。
"""
from curses.ascii import SO


class Solution:
    def robotWithString(self, s: str) -> str:
        """
        t只一个中间栈，借助它对s排序
        找到最小的序。
        能选择的是什么是否从t写到纸上。
        需要一个倒栈，如果后面没有比它更小的字符，那就出栈。
        """
        res = []
        stack = []
        flag = []  #统计当前能否出栈
        min_c = '|'
        for i in range(len(s)-1,-1,-1):
            if s[i] <=min_c:
                min_c = s[i]
            flag.append(min_c)
        flag = flag[::-1]

        for i,c in enumerate(s):
            while stack and stack[-1]<=flag[i]:
                end_c = stack[-1]
                res.append(end_c)
                stack.pop()
            else:
                stack.append(c)
        while stack:
            end_c = stack.pop()
            res.append(end_c)
        return "".join(res)
print(Solution().robotWithString("vzhofnpo"))
# "fnohopzv"
        




