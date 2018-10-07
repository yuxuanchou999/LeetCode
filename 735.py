class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res = []
        for x in asteroids:
            if not res:
                res.append(x)
            elif res[-1] > 0 and x < 0:
                if res[-1] + x > 0:
                    continue
                elif res[-1] > 0 and x < 0:
                    while res and res[-1] + x < 0 and res[-1] >= 0:
                        res.pop()
                    if not res or res[-1] < 0:
                        res.append(x)
                    elif res[-1] + x == 0:
                        res.pop()
            else:
                res.append(x)
                
        return res
