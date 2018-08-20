# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        read, need, buffer = 0, n, [''] * 4
        while need > 0:
            k = read4(buffer)
            need = min(k, n - read)
            buf[read:read + need] = buffer[:need]
            read += need
        return read
