class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        if version1 == version2: return 0
        version1, version2 = version1.split('.'), version2.split('.')
        k = min(len(version1), len(version2))
        for i in range(k):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
       
        if sum([int(i) for i in version1[k:]]) == 0 and sum([int(i) for i in version2[k:]]) == 0 : return 0
        return 1 if len(version1) > len(version2) else -1
