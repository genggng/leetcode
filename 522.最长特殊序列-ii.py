#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start
from curses import flash
from operator import sub
from tokenize import Special


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        """
        关键点：
        每个序列都是自身的子序列；
        特殊序列只能是一个字符串的子序列；
        由此可得，特殊序列只能只自己的子序列，不能是其他的子序列。
        特殊序列没有“爹”

        解法：
        按照长度对所有字符串排序，最长的在前面
        寻找到第一个特殊序列就可结束循环。
        """
        # 按照长度排序
        strs = sorted(strs,key=lambda x:len(x),reverse=True)
        def is_subseq(son,dad):
            # 判断son是不是dad的儿子
            j = 0
            # 子序列的元素一定在父序列里出现
            for i in range(len(son)):
                chr = son[i]  
                try:
                    idx = dad.index(chr,j) #在父序列里查找
                except ValueError:
                    return False  
                else:
                    j = idx+1  # 更新父序列的位置
            return True

        le = len(strs[0])
        find = False
        for i in range(len(strs)):
            le = len(strs[i])  #当前串长度
            special = True  # 默认是孤儿
            for j in range(len(strs)):  # 遍历其他串
                if i == j: continue
                if len(strs[j])<le: break   #比我短，后面都不用看了，肯定不是我爹
                if is_subseq(strs[i],strs[j]):  #找到爹   
                    special = False      #看来我不是孤儿
                    break                 #看下一个是不是
            if special:                  # 找完了，没找到爹 
                find = True              #确定找到了孤儿
                break                   # 不用找了，后面即使有孤儿，也比我短
        return le if find else -1
        


# @lc code=end

