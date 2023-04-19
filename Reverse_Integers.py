class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Check if the input integer is +ve or -ve
        if x < 0:
            str_x = str(abs(x))
            sign=-1
        else:
            str_x = str(x)
            sign=1
        f_x=[]
        # Record the number of digits on the input integer
        n = len(str_x)
        for i in range(n):
            f_x.append(str_x[n-i-1])
        
        str_value = ''.join(f_x)
        str_int = int(str_value)
        
        # Return the reversed integer with proper sign
        return sign*str_int
      

# Case Study 1      
s = Solution()
num = -3257

result = s.reverse(num)
print(result)  # Output: -7523


# Case Study 2      
s = Solution()
num = 412

result = s.reverse(num)
print(result)  # Output: 214
