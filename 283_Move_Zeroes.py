'''
Problem Statement:

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

1: You must do this in-place without making a copy of the array.
2: Minimize the total number of operations.







Approach:

* We should have count of number of zeros in the provided list
* We will keep a counter of index that is zero
* We will iterate through the list and once the value is non-zero, then we will be swap the non-zero value with zero value and increment the counter next zero.

'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        next_zero_index = 0
        
        for n in nums:
            if n!=0:
                nums[next_zero_index] = n
                next_zero_index += 1
        
        for i in range(1, count_zero +1):
            nums[-i] = 0


