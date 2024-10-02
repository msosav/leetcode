class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        if n < 3:
            return False

        min = nums[0]
        med = 2e31

        for i in range(1, n):
            if nums[i] < min:
                min = nums[i]
            elif nums[i] > min:
                if med != 2e31:
                    if med > nums[i]:
                        med = nums[i]
                    elif med != nums[i]:
                        return True
                else:
                    med = nums[i]
        return False
