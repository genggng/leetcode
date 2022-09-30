"""
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
"""

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if s1=="" and s2=="": return True
        if len(s1) != len(s2):return False
        n = len(s1)
        # 遍历n种旋转方式
        for i in range(n):
            match = True
            for j in range(n):
                idx = (j+i)%n
                print(idx,j,s1[idx],s2[j])
                if s1[idx] != s2[j]:
                    match = False
                    break
                    
            if match: return True
        return False

# s1+s1包含了s1所有轮转后的字符串，只用判断s2是否为（s1+s1）的子字符串即可
class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1