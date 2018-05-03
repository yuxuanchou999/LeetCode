from heapq import *
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        def addsky(pos, hei):
            if sky[-1][1] != hei:
                sky.append([pos, hei])

        sky = [[-1,0]]

        # possible corner positions
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])

        # live buildings
        live = []

        i = 0

        for t in sorted(position):

            # add the new buildings whose left side is lefter than position t
            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            # remove the past buildings whose right side is lefter than position t
            while live and live[0][1] <= t:
                heappop(live)

            # pick the highest existing building at this moment
            h = -live[0][0] if live else 0
            addsky(t, h)

        return sky[1:]

       def getSkyline2(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heappop(hp)
            if negH: 
                heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]
