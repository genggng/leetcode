from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        values = cnt.values()
        double_cnt = Counter(values)
        if len(double_cnt) == 1 and list(double_cnt.keys())[0] == 1:
            return True
        if len(double_cnt) == 2:
            a,b = double_cnt.keys()
            if a<b:  # a>b
                a,b = b,a
            if a-b == 1 and double_cnt[a] == 1:
                return True
        return False


s = "bac"
print(Solution().equalFrequency(s))