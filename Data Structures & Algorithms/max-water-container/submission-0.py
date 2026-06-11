class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights)-1
        print(right)
        containerHeight = left

        while(left < right):
            containerHeight = min(heights[left], heights[right])
            area = containerHeight * abs(left-right)
            maxArea = max(maxArea, area)
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea