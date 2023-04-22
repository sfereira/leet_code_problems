class Solution:
    def removeElement(self, nums, val):
        k=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            nums[k]=nums[i]     
            
            k+=1
        
        # Returns length of the list after removing the target element from the input list    
        return k
      
      
# Case Study 1
s = Solution()
nums = [3,2,2,3]
val = 3
result = s.removeElement(nums,val)
print(result) # Output: 2

# Case Study 2
s = Solution()
nums = [1,4,0,2,4,4,1]
val = 4
result = s.removeElement(nums,val)
print(result) # Output: 4

# Case Study 3
s = Solution()
nums = [1,0,1]
val = 1
result = s.removeElement(nums,val)
print(result) # Output: 1
