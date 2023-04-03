#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        country_flag = ["","+*-","+**-","+***-"]
        if '@' in s:
        # 是个邮件地址
            s = s.lower() #转小写
            name,ext = s.split("@")
            new_name = name[0] + "*****" + name[-1]
            return f"{new_name}@{ext}"
        else:
            num_list = []
            for c in s:
               if c.isdigit():
                   num_list.append(c)
            idx = len(num_list) - 10
            prex = country_flag[idx]
            end = "".join(num_list[-4:])
            return f"{prex}***-***-{end}"
           
                 

# @lc code=end

