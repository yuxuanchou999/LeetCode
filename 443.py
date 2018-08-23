class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i, j, cnt = 0, 0, 0
        while i < len(chars):
            if i == 0:
                cnt = 1
                j += 1
            else:
                if chars[i - 1] != chars[i]:
                    if cnt > 1:
                        for x in list(str(cnt)):
                            chars[j] = x
                            j += 1
                    chars[j] = chars[i]
                    j += 1
                    cnt = 1
                else:
                    cnt += 1
            i += 1
        if cnt > 1:
            for x in list(str(cnt)):
                chars[j] = x
                j += 1
        return j
       
