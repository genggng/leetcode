#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#

# @lc code=start
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        context_map_path = {}
        res = []
        for path in paths:
            words = path.split()
            dir_path = words[0]
            for file in words[1:]:
                file_name,context = file[:-1].split('(')
                if context not in context_map_path.keys():
                    context_map_path[context] = []
                context_map_path[context].append(dir_path+'/'+file_name)
        for paths in context_map_path.values():
            if len(paths) >=2 :
                res.append(paths)
        
        return res
                    
        
# @lc code=end

