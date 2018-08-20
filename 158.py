# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.queue = []
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read, need, buffer = 0, n, [""] * 4
        while need:
            k = read4(buffer)
            self.queue.extend(buffer[:k])
            need = min(len(self.queue), n - read)
            buf[read: read + need] = [self.queue.pop(0) for _ in range(need)]
            read += need
        return read            
            
