class Solution:
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def helper(nest, depth):
            ans = 0
            for x in nest:
                if x.isInteger():
                    ans += x.getInteger() * depth
                else:
                    ans += helper(x.getList(), depth + 1)
            return ans
        

        return helper(nestedList, 1)
