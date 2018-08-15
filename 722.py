class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        block, res, newline = False, [], []
        for line in source:
            i = 0
            while i < len(line):
                if not block and i + 1 < len(line) and line[i:i + 2] == '/*':
                    block = True
                    i += 1
                elif block and i + 1 < len(line) and line[i:i + 2] == '*/':
                    block = False
                    i += 1
                elif not block and i + 1 < len(line) and line[i:i + 2] == '//':
                    break
                elif not block:
                    newline.append(line[i])
                i += 1
            if newline and not block:
                res.append(''.join(newline))
                newline = []
        return res
