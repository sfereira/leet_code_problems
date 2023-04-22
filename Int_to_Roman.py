class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Storing roman values of digits from 0-9
        # when placed at different places
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", \
             "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L", \
             "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", \
             "VI", "VII", "VIII", "IX"]

        # Converting to roman
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]

        roman = (thousands + hundreds + tens + ones)

        roman = roman.replace(" ","")

        return roman
      

# Case Study 1
s = Solution()
result = s.intToRoman(1994)
print(result) # Output --> MCMXCIV


# Case Study 2
s = Solution()
result = s.intToRoman(54)
print(result) # Output --> LIV


# Case Study 3
s = Solution()
result = s.intToRoman(145)
print(result) # Output --> CXLV

