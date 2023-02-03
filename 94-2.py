"""
6274. 奖励最顶尖的 K 名学生 显示英文描述 

题目难度Medium
给你两个字符串数组 positive_feedback 和 negative_feedback ，分别包含表示正面的和负面的词汇。不会 有单词同时是正面的和负面的。

一开始，每位学生分数为 0 。每个正面的单词会给学生的分数 加 3 分，每个负面的词会给学生的分数 减  1 分。

给你 n 个学生的评语，用一个下标从 0 开始的字符串数组 report 和一个下标从 0 开始的整数数组 student_id 表示，其中 student_id[i] 表示这名学生的 ID ，这名学生的评语是 report[i] 。每名学生的 ID 互不相同。

给你一个整数 k ，请你返回按照得分 从高到低 最顶尖的 k 名学生。如果有多名学生分数相同，ID 越小排名越前。

 
"""
from typing import List
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        res = []
        for i in range(len(report)):
            msg = report[i]
            id = student_id[i]
            score = 0
            for word in msg.split():
                if word in positive_feedback:
                    score += 3
                if word in negative_feedback:
                    score -= 1
            res.append((id,score))
        res.sort()
        res.sort(key=lambda x:x[1],reverse=True)
        ids = list(zip(*res))[0]
        return ids[:k]    
   
positive_feedback = ["fkeofjpc","qq","iio"]
negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"]
report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"]
student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263]
k = 3
print(Solution().topStudents(positive_feedback,negative_feedback,report,student_id,k))