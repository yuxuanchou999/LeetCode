class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a, new, cnt = [], '', 0
        for w in words:
            new = ''
            for i in w:
                new += ref[ord(i) - ord('a')]
            if new not in a:
                a.append(new)
                cnt += 1
                
        return cnt
