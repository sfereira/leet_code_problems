# Given two integer arrays 'pushed' and 'popped' each with distinct values, 
# return 'true' if this could have been the result of a sequence of push and pop operations on an initially empty stack, 
# or 'false' otherwise.

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack_list=[]  # holding list
        count = 0  # counter
        
        for num in pushed:
            stack_list.append(num)

            while stack_list and stack_list[-1] == popped[count]:
                stack_list.pop()
                # increment the counter
                count +=1
        
        # return boolean
        return count == len(popped)
      
# Case Study 1        
s = Solution()
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
result = s.validateStackSequences(pushed, popped)
print(result) # expected result -> true
      
# Case Study 2        
s = Solution()
pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
result = s.validateStackSequences(pushed, popped)
print(result) # expected result -> false
