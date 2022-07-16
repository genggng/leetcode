# https://leetcode.cn/problems/qIsx9U/

"""
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。

实现 MovingAverage 类：

MovingAverage(int size) 用窗口大小 size 初始化对象。
double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。

"""
from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size  #滑动大小
        self.q = deque([])  #滑动窗口
        self.sum = 0.0
        self.num = 0


    def next(self, val: int) -> float:
        self.q.append(val)
        self.sum += val
        if self.num == self.size:
            self.sum -= self.q.popleft()
        else:
            self.num += 1
        return self.sum / self.num