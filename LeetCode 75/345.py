class Solution(object):
    def isVowel(self, si):
        if si.lower() == "a" or si.lower() == "e" or si.lower() == "i" or si.lower() == "o" or si.lower() == "u":
            return True
        return False

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        l = 0
        r = len(s) - 1

        s = list(s)

        while (l < r + 1):
            if (self.isVowel(s[l])):
                if (self.isVowel(s[r])):
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                else:
                    r -= 1
            elif (self.isVowel(s[r])):
                if (self.isVowel(s[l])):
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                else:
                    l += 1
            else:
                l += 1
                r -= 1
        
        return ''.join(s)
