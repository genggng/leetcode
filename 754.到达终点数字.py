#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#

# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:
        """
        1. target为整数或者负数对称，只用考虑target为正数即可。
        2. 最小步数为k,s = sum(list(range(k))) >= target
        3. s-target为偶数才有可能刚好到达，因为把任意一个正数i翻转为负数，s都会减少2*i
        4. 找到第一个使s-target为偶数的值，判断(s-target)/2 能否为前面若干数字的和。
        5. 前k个数，能够任意算出部分数，其和的范围为[1,sk]
        """

        """
        73/73 cases passed (144 ms)
        Your runtime beats 10.67 % of python3 submissions
        Your memory usage beats 33.71 % of python3 submissions (14.9 MB)
        """
        # target = abs(target)
        # s = 1
        # k = 1
        # while True:
        #     if s >= target and (s-target)%2 == 0:
        #         return k
        #     s = s * (k+2) // k
        #     k = k+1
        """
        继续优化，能够更快地找到k。
        解方程(k+1)*k/2 >= 2*t => k>= sqrt(2*t+1/4) - 1/2
        s对k以4为周期，呈现[奇数，奇数，偶数，偶数]排列，如果想让差值为偶数，s和target奇偶性应该相同。
        只需要找到在k后的第一个周期使奇偶性相同的数值。
        """
        target = abs(target)
        k = int((2*target + 0.25)** 0.5 - 0.5)
        s = (k+1)*k //2
        if s < target:
            k += 1
        t_attr = bool(target%2) # target的奇偶性
        s_attr = bool((k-1)%4 <2) #s的奇偶性
        if s_attr == t_attr: #奇偶性相同
            return k
        else:   #奇偶性不同，k向后最多移动2位。
            # k为奇数，向后移动2位，k为偶数向后移动一位，
            k += 1 if k%2 == 0 else 2
            return k
        """
        速度提升了4倍。
        73/73 cases passed (36 ms)
        Your runtime beats 93.82 % of python3 submissions
        Your memory usage beats 6.74 % of python3 submissions (15 MB)
        """

# @lc code=end

