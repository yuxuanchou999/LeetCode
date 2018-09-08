class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for i in range(len(A)):
            odd, even = '', ''
            for j in range(len(A[i])):
                if j % 2: odd += A[i][j]
                else: even += A[i][j]
            dic[''.join(sorted(even)) + ''.join(sorted(odd))] += 1
        return len(dic)
            
