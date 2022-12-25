"""
6295. 最小化两个数组中的最大值 显示英文描述 
题目难度Medium
给你两个数组 arr1 和 arr2 ，它们一开始都是空的。你需要往它们中添加正整数，使它们满足以下条件：

arr1 包含 uniqueCnt1 个 互不相同 的正整数，每个整数都 不能 被 divisor1 整除 。
arr2 包含 uniqueCnt2 个 互不相同 的正整数，每个整数都 不能 被 divisor2 整除 。
arr1 和 arr2 中的元素 互不相同 。
给你 divisor1 ，divisor2 ，uniqueCnt1 和 uniqueCnt2 ，请你返回两个数组中 最大元素 的 最小值 。
"""
class Solution:
    """
    二分查找
    """
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        l, r = 0, int(1e18)
        
        def chk(k):
            a = k // divisor1
            b = k // divisor2
            c = k // lcm(divisor1, divisor2)
            m = k - a - b + c
            a -= c
            b -= c
            a = min(uniqueCnt2, a)
            b = min(uniqueCnt1, b)
            # print(a, b, m)
            return m + a + b >= uniqueCnt1 + uniqueCnt2
        # chk(8)
        while l < r:
            mid = (l + r) // 2
            if chk(mid):
                r = mid
            else:
                l = mid + 1
        return l


divisor1 = 9
divisor2 = 4
uniqueCnt1 = 8
uniqueCnt2 = 3
print(Solution().minimizeSet(divisor1,divisor2,uniqueCnt1,uniqueCnt2))