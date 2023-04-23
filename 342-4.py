from typing import List
"""
6390. 滑动子数组的美丽值 显示英文描述 
给你一个长度为 n 的整数数组 nums ，请你求出每个长度为 k 的子数组的 美丽值 。

一个子数组的 美丽值 定义为：如果子数组中第 x 小整数 是 负数 ，那么美丽值为第 x 小的数，否则美丽值为 0 。

请你返回一个包含 n - k + 1 个整数的数组，依次 表示数组中从第一个下标开始，每个长度为 k 的子数组的 美丽值 。

子数组指的是数组中一段连续 非空 的元素序列。

 

示例 1：

输入：nums = [1,-1,-3,-2,3], k = 3, x = 2
输出：[-1,-2,-2]
解释：总共有 3 个 k = 3 的子数组。
第一个子数组是 [1, -1, -3] ，第二小的数是负数 -1 。
第二个子数组是 [-1, -3, -2] ，第二小的数是负数 -2 。
第三个子数组是 [-3, -2, 3] ，第二小的数是负数 -2 。
示例 2：

输入：nums = [-1,-2,-3,-4,-5], k = 2, x = 2
输出：[-1,-2,-3,-4]
解释：总共有 4 个 k = 2 的子数组。
[-1, -2] 中第二小的数是负数 -1 。
[-2, -3] 中第二小的数是负数 -2 。
[-3, -4] 中第二小的数是负数 -3 。
[-4, -5] 中第二小的数是负数 -4 。
示例 3：

输入：nums = [-3,1,2,-3,0,-3], k = 2, x = 1
输出：[-3,0,-3,-3,-3]
解释：总共有 5 个 k = 2 的子数组。
[-3, 1] 中最小的数是负数 -3 。
[1, 2] 中最小的数不是负数，所以美丽值为 0 。
[2, -3] 中最小的数是负数 -3 。
[-3, 0] 中最小的数是负数 -3 。
[0, -3] 中最小的数是负数 -3 。
 

提示：

n == nums.length 
1 <= n <= 105
1 <= k <= n
1 <= x <= k 
-50 <= nums[i] <= 50 
"""
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []
        def quicksort(num ,low ,high):  #快速排序
            if low< high:
                location = partition(num, low, high)
                quicksort(num, low, location - 1)
                quicksort(num, location + 1, high)
        
        def partition(num, low, high):
            pivot = num[low]
            while (low < high):
                while (low < high and num[high] > pivot):
                    high -= 1
                while (low < high and num[low] < pivot):
                    low += 1
                temp = num[low]
                num[low] = num[high]
                num[high] = temp
            num[low] = pivot
            return low
        
        def findkth(num,low,high,k):   #找到数组里第k个数
                index=partition(num,low,high)
                if index==k:return num[index]
                if index<k:
                    return findkth(num,index+1,high,k)
                else:
                    return findkth(num,low,index-1,k)
        tmp = []
        for num in nums[0:k]:
            if num<0:
                tmp.append(num)

        for l in range(len(nums)-k+1):
            
            ready = True
            if nums[l]<0:
                tmp = []
                for num in nums[l:k+l]:
                    if num<0:
                        tmp.append(num)
                ready = False
            if x>len(tmp):
                val = 0
            else:
                if len(tmp)<1000:
                    if not ready:
                        tmp.sort()
                    val = tmp[x-1]
                else:
                    val = findkth(tmp,0,len(tmp)-1,x-1)
            res.append(val)
        return res
    
nums = [1,-1,-3,-2,3]
k = 3
x = 2
print(Solution().getSubarrayBeauty(nums,k,x))
