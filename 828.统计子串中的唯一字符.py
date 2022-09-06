#
# @lc app=leetcode.cn id=828 lang=python3
#
# [828] 统计子串中的唯一字符
#

# @lc code=start
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        思考每种字符对最终结果的贡献
        每种字符在子字符串中出现一次，就能提供1点贡献
        各种字符串提供的贡献相互独立，并不会互相影响
        只用统计每种字符串对最终结果的贡献即可
        """
        index = {}
        for i,c in enumerate(s):
            if c not in index.keys():
                index[c] = []
            index[c].append(i)  #将相同字符的索引放入一个列表
        
        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]  #给出s数组的起始结束边界
            for i in range(1,len(arr)-1):
                # arr[i] 存储的是字符arr存在的位置
                # 对于arr 存在的三个位置i,j,k  其存在arr的子字符串有 (arr[j] - arr[i])*(arr[k] - arr[j])
                # 即起始位置有(arr[j] - arr[i]) 种 结束位置有arr[k] - arr[j] 种可能，保证字符串中只包含一个arr
                res += (arr[i] - arr[i-1])*(arr[i+1]-arr[i])
        return res
# @lc code=end

