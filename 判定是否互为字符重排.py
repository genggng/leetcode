#给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串
from collections import Counter
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        count1 = Counter(list(s1))
        count2 = Counter(list(s2))
        if len(count1.keys()) != len(count2.keys()):
            return False
        for key in count1.keys():
            if count1[key] != count2[key]:
                return False
        return True
a = "abc"
b = "cab"
print(Solution().CheckPermutation(a,b))