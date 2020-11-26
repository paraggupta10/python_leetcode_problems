'''
Problem Statement:

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2




Approach:



'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        seen = {}
        
        if len(nums) == 1:
            return nums[0]
        
        for n in nums:
            if n in seen:
                seen[n] += 1
                if seen[n] > ( len(nums) / 2):
                    return n
            else:
                seen[n] = 1
                
