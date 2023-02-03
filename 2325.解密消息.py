#
# @lc app=leetcode.cn id=2325 lang=python3
#
# [2325] 解密消息
#

# @lc code=start
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        decode_c = ord("a")
        map_dict = {}
        end = ord("z")
        for c in key:
            if c == " ":
                continue
            if c not in map_dict.keys():
                map_dict[c] = chr(decode_c)
                decode_c += 1
                if decode_c > end:
                    break
        res = []
        for c in message:
            if c == " ":
                res.append(c)
            else:
                res.append(map_dict[c])
        return "".join(res)
# @lc code=end

