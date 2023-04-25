#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#

# @lc code=start
from collections import Counter
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        
    def query(self, left: int, right: int, threshold: int) -> int:
        cnt = Counter(self.arr[left:right+1])
        res = -1
        for k,v in cnt.items():
            if v >= threshold:
                res = k
                break
        return res


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end

