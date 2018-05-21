class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefix = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefix for p in prefix)
            
        return answer
