class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = r = len(s) - 1
        reversed_string = ""
        first = 0

        if len(s) == 1 and s[0] != " ":
            return s

        while l > 0:
            if s[l] == " " and s[r] != " ":
                if first == 0:
                    reversed_string += s[l+1:r+1]
                    first = 1
                else:
                    reversed_string += " " + s[l+1:r+1]
                while s[l] == " ":
                    l -= 1
                r = l
            elif s[l] == " " and s[r] == " ":
                l -= 1
                r -= 1
            else:
                l -= 1

            if l == 0 and s[l] != " ":
                if first != 0:
                    reversed_string += " " + s[0:r+1]
                else:
                    reversed_string += s[0:r+1]
            elif l == 0 and s[l] == " ":
                if first != 0:
                    reversed_string += " " + s[1:r+1]
                else:
                    reversed_string += s[1:r+1]

        return reversed_string
