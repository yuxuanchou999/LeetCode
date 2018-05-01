class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        """
        vertical
        """
        # if not strs:
        #     return ""
        # for i in range(len(strs[0])):
        #     for string in strs[1:]:
        #         if i >= len(string) or strs[0][i] != string[i]:
        #             return strs[0][:i]
        # return strs[0]
        """
        horizontal
        """
        if not strs:
            return ""
        l = len(strs[0])
        for string in strs:
            for i in range(l):
                if i >= len(string) or string[i] != strs[0][i]:
                    l = i
                    break
        return strs[0][:l]
