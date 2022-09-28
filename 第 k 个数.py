"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。
"""

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        """
        待寻找的数，都是由若干个3,5,7乘积获得。
        关键是合并三个有序列表
        """
        num_list = [0]*(k+1)
        num_list[0] = 1
        p3,p5,p7 = 0,0,0 #三个指针，指出3,5,7从那个num_list生成的
        for i in range(1,k+1):
            new_num = min([num_list[p3]*3,num_list[p5]*5,num_list[p7]*7]) #生成新数
            if new_num == num_list[p3]*3: p3+=1
            if new_num == num_list[p5]*5: p5+=1
            if new_num == num_list[p7]*7: p7+=1
            num_list[i] = new_num
        return num_list[k-1]