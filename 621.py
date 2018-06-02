class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = [tasks.count(i) for i in set(tasks)]
        ans = (n + 1) * (max(cnt) - 1)
        for i in cnt:
            if i == max(cnt):
                ans += 1
        return max(ans, len(tasks))
