class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k == 1: return [i for i in range(1, n + 1)]
        cnt, res, i = k + 1, [k + 1], 1
        while k > 0:
            if i % 2:
                cnt -= k
            else:
                cnt += k
            res.append(cnt)
            k -= 1
            i += 1
        res += [i for i in range(res[0] + 1, n + 1)]
        return res
