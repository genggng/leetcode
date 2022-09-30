"""
给你一个字符串数组 names ，和一个由 互不相同 的正整数组成的数组 heights 。两个数组的长度均为 n 。

对于每个下标 i，names[i] 和 heights[i] 表示第 i 个人的名字和身高。

请按身高 降序 顺序返回对应的名字数组 names 。

"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        comb = list(zip(names,heights))
        res,_ = zip(*sorted(comb,key=lambda x: x[1],reverse=True))
        return res