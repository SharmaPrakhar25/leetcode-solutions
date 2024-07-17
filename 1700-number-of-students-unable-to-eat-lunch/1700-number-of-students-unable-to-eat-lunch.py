import collections

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentMap = Counter(students)
        res = len(students)
            
        for s in sandwiches:
            if studentMap[s] > 0:
                res -= 1
                studentMap[s] -= 1
            else:
                return res
            
        return res