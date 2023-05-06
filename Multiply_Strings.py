## Multiply Strings

#### Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

#### Note: *You must not use any built-in BigInteger library or convert the inputs to integer directly.*

## Constraints:

"""
1. `1 <= num1.length, num2.length <= 200`
2. `num1` and `num2` consist of digits only.
3. Both `num1` and `num2` do not contain any leading zero, except the number `0` itself.
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        digit_dict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        n1=0
        n2=0
        for i in num1:
            val = digit_dict.get(i)
            n1 = n1*10 + val
        
        for i in num2:
            val = digit_dict.get(i)
            n2 = n2*10 + val
        
        n3 = n1 * n2
        
        val_list = list(digit_dict.values())
        key_list = list(digit_dict.keys())
        
        result=""
        
        if n3 == 0:
            result = "0"
            return result
        
        while n3 >= 1:
            rem = n3%10
            for digit in digit_dict:
                if digit_dict.get(digit) == rem:
                    result = digit + result
            n3 = n3//10
        
        return result
      
# Case Study 1
s = Solution()
num1, num2 = '3','2'
result = s.multiply(num1, num2)
print(result,type(result)) # Output: "6" <class 'str'>

# Case Study 2
s = Solution()
num1, num2 = '123','456'
result = s.multiply(num1, num2)
print(result,type(result)) # Output: "56088" <class 'str'>

# Case Study 3
s = Solution()
num1, num2 = '100','5'
result = s.multiply(num1, num2)
print(result,type(result)) # Output: "500" <class 'str'>
