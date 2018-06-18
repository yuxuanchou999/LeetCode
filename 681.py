class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digit = [x for x in set(time) if x != ':']
        digit.sort()
        for x in digit:
            for y in digit:
                if x + y < '60' and x + y > time[-2:]:
                    return time[:3] + x + y
            
        for x in digit:
            for y in digit:
                if x + y > time[:2] and x + y < '24':
                    return x + y + ':' + digit[0] * 2
        return digit[0] * 2 + ':' + digit[0] * 2
