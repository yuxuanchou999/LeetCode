class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return [a+b if c == '+' else a-b if c == '-' else a*b
                    for i, c in enumerate(input) if c in '+-*'
                    for a in self.diffWaysToCompute(input[:i])
                    for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]




    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\D)', input)
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+': operator.add, '-': operator.sub, '*': operator.mul}.get, tokens[1::2]))
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b)
                    for i in xrange(lo, hi)
                    for a in build(lo, i)
                    for b in build(i + 1, hi)]
        return build(0, len(nums) - 1)
