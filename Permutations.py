#
# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.
#
# Constraints:
#
# 1. ` 1 <= nums.length <= 6 `
# 2. ` -10 <= nums[i] <= 10 `
# 3. All the `integers` of nums are `unique`.
#

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        
        nlist=[]
        
        if n == 0:
            return nlist
        elif n == 1:
            nlist = [nums]
            return nlist
        else:
            for i in range(n):
                k = nums[i]
                m = nums[:i] + nums[i+1:]
                for j in self.permute(m):
                    nlist.append([k]+j)
                    
        return nlist
      

# Case Study 1
s = Solution()
nums=[1,2,3]
result = s.permute(nums)
print(result) # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# Case Study 2
s = Solution()
nums=[0,1]
result = s.permute(nums)
print(result) # Output: [[0, 1], [1, 0]]

# Case Study 3
s = Solution()
nums=[1]
result = s.permute(nums)
print(result) # Output: [[1]]

