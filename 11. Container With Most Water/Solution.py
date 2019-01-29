class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0;
        end = len(height)-1;
        result = 0;
        while start <= end :
            currentCapacity = min(height[start], height[end])*(end-start);
            if currentCapacity > result:
                result = currentCapacity;
            if height[start] >= height[end]:
                end = end-1;
            else:
                start = start + 1;
        return result;