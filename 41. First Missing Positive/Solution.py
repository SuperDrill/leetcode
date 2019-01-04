class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) + 1
        for i in range(0, n-1):
            nums[i] = 0 if nums[i] <= 0 or nums[i] >= n else nums[i]
        for i in range(0, n-1):
            if nums[i] > 0:
                nums[nums[i]%n-1] += n
        for i in range(0,n-1):
            if nums[i] < n:
                return i+1
        return n