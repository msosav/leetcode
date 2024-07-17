class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        if len(word1) > len(word2):
            n = len(word1)
        else:
            n = len(word2)

        merged_string = ""

        for i in range(n):
            if i > len(word1) - 1:
                merged_string += word2[i:]
                break
            elif i > len(word2) - 1:
                merged_string += word1[i:]
                break
            else:
                merged_string += word1[i] + word2[i]

        return merged_string