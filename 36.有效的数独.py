#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set([]) for _ in range(9)]
        col_set = [set([]) for _ in range(9)]
        local_set = [[set([]) for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if not num.isdigit():
                    continue
                
                if num in row_set[i]:
                    return False
                row_set[i].add(num)

                if num in col_set[j]:
                    return False
                col_set[j].add(num)

                if num in local_set[i//3][j//3]:
                    return False
                local_set[i//3][j//3].add(num)
        return True

# @lc code=end

