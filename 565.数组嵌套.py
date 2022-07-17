#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        提供了一个等价关系，给数组中元素分类。
        其实就是数组中元素形成一个个的圆环，找到最大的环。
        """
        res = 0
        n = len(nums)
        cricle = set()
        nodes = set(nums)
        while nodes:
            x = list(nodes)[0]
            while nums[x] not in cricle: #没有出现环
                cricle.add(nums[x])
                x = nums[x]
            else:
                res = max(res,len(cricle)) #更新最大环长度
                if res >= n/2:  #不会有更大的，直接返回
                    return res
                nodes = nodes - cricle
                # print(cricle)
                cricle = set()
                
        return res

# @lc code=end

