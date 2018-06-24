class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        root, content = collections.defaultdict(list), collections.defaultdict(list)
        for x in paths:
            cnt = 0
            for i in range(len(x)):
                if cnt == 0 and x[i] == ' ':
                    r = x[:i] + '/'
                    cnt = i + 1
                elif x[i] == ')' or i == len(x) - 1:
                    root[x[cnt:st]].append(r)
                    content[x[st:i + 1]].append(x[cnt:st])
                    cnt = i + 2
                elif x[i] == '(':
                    st = i
        
        return [[root[y].pop(0) + y for y in content[x]] for x in content if len(content[x]) > 1]
                
        
