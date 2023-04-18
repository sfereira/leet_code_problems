class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # start and end points of the palindrome string
        start,end = 0,0
        
        n = len(s)
        
        for i in range(n):
            # Check odd length palindromes
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                if r - l - 1 > end - start:
                    start, end = l + 1, r
            
            # Check even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                if r - l - 1 > end - start:
                    start, end = l + 1, r
        
        # Return the largest palindrome string
        return s[start:end]
      

# Case Study 1      
s = Solution()
word = 'babad'

result = s.longestPalindrome(word)
print(result)  # Output: 'bab'   


# Case Study 2
s = Solution()
word = 'cbbd'

result = s.longestPalindrome(word)
print(result) # Output: 'bb'
