# Time Complexity : O(n), where n is the length of the array
# Space Complexity : O(1), in-place sorting with constant space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # I used the Dutch National Flag algorithm with three pointers
        start, read = 0, 0
        end = len(nums) - 1

        while read <= end:
            if nums[read] == 0:
                nums[read], nums[start] = nums[start], nums[read]
                start += 1
                read += 1
            elif nums[read] == 2:
                nums[read], nums[end] = nums[end], nums[read]
                end -= 1
            else:
                read += 1
