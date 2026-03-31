class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxStored = 0
        while(l < r):
            maxStored = max(maxStored, min(heights[l], heights[r]) * (r - l))
            if(heights[l] > heights[r]):
                r -= 1
            else:
                l += 1
        return maxStored