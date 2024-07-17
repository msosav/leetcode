class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1 = len(str1)
        len2 = len(str2)

        def is_divisor(l):
            if len1 % l != 0 and len2 % l != 0:
                return False
            f1 = len1 / l
            f2 = len2 / l
            if f1 * str1[:l] == str1 and f2 * str1[:l] == str2:
                return True

        for l in range(min(len1, len2), 0, -1):
            if is_divisor(l):
                return str1[:l]

        return ""
