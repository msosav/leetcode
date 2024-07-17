class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        bool_list = []
        max_candies = 0
        for i in range(len(candies)):
            if candies[i] > max_candies:
                max_candies = candies[i]

        for i in range(len(candies)):
            extra_candies = candies[i] + extraCandies
            if extra_candies >= max_candies:
                bool_list.append(True)
            else:
                bool_list.append(False)

        return bool_list
