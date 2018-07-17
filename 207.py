class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        zero_in_degree, in_degree, out_degree = [], {}, {}
        for i, j in prerequisites:
            if i not in in_degree:
                in_degree[i] = set()
            if j not in out_degree:
                out_degree[j] = set()
            in_degree[i].add(j)
            out_degree[j].add(i)
            
        for i in range(numCourses):
            if i not in in_degree:
                zero_in_degree.append(i)
                
        while zero_in_degree:
            pre = zero_in_degree.pop()
            if pre in out_degree:
                for course in out_degree[pre]:
                    in_degree[course].discard(pre)
                    if not in_degree[course]:
                        zero_in_degree.append(course)
                del out_degree[pre]
        
        return False if out_degree else True
        
            
                
