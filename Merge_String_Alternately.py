class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len_word1 = len(word1) # length of string 1
        len_word2 = len(word2) # length on string 2
        new_string=[] # empty list to hold final merged string
        if len_word1 > len_word2:
            # If string 1 has more characters than string 2
            i = 0 
            j = 0
            while i < len_word1:
                new_string.append(word1[i])
                if j < len_word2:
                    new_string.append(word2[j])
                else:
                    pass
                i +=1
                j +=1
        elif len_word2 > len_word1:
            # If string 2 has more characters than string 1
            i = 0 
            j = 0
            while i < len_word2:
                if j < len_word1:
                    new_string.append(word1[j])
                else:
                    pass
                new_string.append(word2[i])
                i +=1
                j +=1
        else:
            # If string 1 and string 2 have same number of characters
            for i in range(len_word1):
                new_string.append(word1[i])
                new_string.append(word2[i])
        
        # Convert the final merged list of characters into a single string
        str_value = ''.join(new_string)
        return str_value
