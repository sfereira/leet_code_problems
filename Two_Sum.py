# Given an array of integers `nums` and an integer `target`, return `indices` of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of the input numbers
        indices_dict = {}
        
        # i is for index and number is for actual input element corresponding
        for i, number in enumerate(nums):
            # Calculate the value needed to reach the target
            value = target - number
            
            # Check if the value is already in the dictionary and not at the same index as the selected one
            if value in indices_dict and indices_dict[value] != i:
                # If condition True, return the current index and the value's index
                return [indices_dict[value], i]
            else:
                # Else, add the current number index to the dictionary
                indices_dict[number] = i
        
        # If input elements cannot find solution that matches the target, return an empty list
        return []
        
# Case Study 1        
s = Solution()
nums = [2, 7, 11, 15]
target = 9
result = s.twoSum(nums, target)
print(result)

# Case Study 2
s = Solution()
nums = [3,2,4]
target = 6
result = s.twoSum(nums, target)
print(result)

# Case Study 3
s = Solution()
nums = [3,3]
target = 6
result = s.twoSum(nums, target)
print(result)
