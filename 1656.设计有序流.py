#
# @lc app=leetcode.cn id=1656 lang=python3
#
# [1656] 设计有序流
#

# @lc code=start
class OrderedStream:

    def __init__(self, n: int):
        # self.id_list = [0]*(n+1)  #标志是否存在数字
        self.n = n
        self.ptr = 1
        self.values = [""]*(n+1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.values[idKey] = value
        if self.ptr == idKey:
            start = self.ptr
            for i in range(idKey,self.n+1):
                if self.values[i] == "":
                    self.ptr = i
                    return self.values[start:self.ptr]
            self.ptr = self.n+1
            return self.values[start:]
        else:
            return []


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# @lc code=end

