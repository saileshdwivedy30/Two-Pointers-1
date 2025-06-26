# Time Complexity : O(n), where n is the number of elements in the height array
# Space Complexity : O(1), uses constant space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # I used the two-pointer approach starting from both ends
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area between the two lines
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            # Move the pointer that has the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
