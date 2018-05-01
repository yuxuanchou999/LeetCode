class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abbahbfcw'))
