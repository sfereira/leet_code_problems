# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# Return the 'quotient' after dividing 'dividend' by 'divisor'.
# Constraints:
# 1. -231 <= dividend, divisor <= 231 - 1
# 2. divisor != 0
# 3. if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            sign = -1
        else:
            sign = 1
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            quotient = dividend
        else:
            # If Python 2 then
            #quotient = len(xrange(0,(dividend-divisor)+1,divisor))
            
            # If Python 3 then
            quotient = len(range(0,(dividend-divisor)+1,divisor))

        if sign == -1:
            quotient = - quotient

        if quotient <= -2**31:
            quotient = -2**31
        elif quotient >= (2**31)-1:
            quotient = (2**31)-1

        return quotient
      

# Case Study 1
s = Solution()
dividend = 10
divisor = 3
result = s.divide(dividend,divisor)
print(result) # Output : 2

# Case Study 2
s = Solution()
dividend = 7
divisor = -3
result = s.divide(dividend,divisor)
print(result) # Output : -2

# Case Study 3
s = Solution()
dividend = 2522
divisor = -13
result = s.divide(dividend,divisor)
print(result) # Output : -194
