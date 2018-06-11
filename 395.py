class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def helper(s, k, start, end):
            count = [0] * 26
            for x in s[start:end]:
                count[ord(x) - ord('a')] += 1
            i, maxlen = start, 0
            while i < end:
                while i < end and count[ord(s[i]) - ord('a')] < k:
                    i += 1
                j = i
                while j < end and count[ord(s[j]) - ord('a')] >= k:
                    j += 1
                if i == start and j == end: return end - start
                maxlen = max(maxlen, helper(s, k, i, j))
                i = j
            return maxlen
        
        return helper(s, k, 0, len(s))
