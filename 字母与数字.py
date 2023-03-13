"""
给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
"""
class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        new_array = [0]
        presum = []
        tmp = 0
        for i in range(len(array)):
            if array[i].isdigit():
                new_array.append(-1)
            else:
                new_array.append(1)
            tmp += new_array[i+1]
            presum.append(tmp)  #前缀和

        # 寻找长度最长的和为0子数组array[i:j]。
        for i in range(len(array)-1):
            j = len(new_array)
            while j > i:
                if presum[j] - presum[i] == 0:
                    return array[i:j]
        return []
