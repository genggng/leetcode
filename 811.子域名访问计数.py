#
# @lc app=leetcode.cn id=811 lang=python3
#
# [811] 子域名访问计数
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """
        最朴素的想法，以子域名为key建立哈希表
        """
        domian_dict = dict()
        for cpdomain in cpdomains:
            count, domians = cpdomain.split()
            count = int(count)
            domian_list = domians.split(".")
            for i in range(len(domian_list)):
                key = ".".join(domian_list[i:])
                if key not in domian_dict.keys():
                    domian_dict[key] = 0
                domian_dict[key] += count
        res = [f"{count} {domain}" for domain,count in domian_dict.items()]
        return res
# @lc code=end

