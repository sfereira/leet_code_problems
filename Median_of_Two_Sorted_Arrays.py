# Given two sorted arrays 'nums1' and 'nums2' of size 'm' and 'n' respectively, return the median of the two sorted arrays.
# The overall run time complexity should be 'O(log (m+n))'.

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)  # Combine both input list into one
        new_list = sorted(nums1)  # Sort the combined list ascending order
        n = len(new_list)  # Total number of elements in the sorted list
        
        # Even number of elements
        if n % 2 == 0:
            l1 = n // 2
            l2 = l1 - 1
            med = (new_list[l1] + new_list[l2])*0.5
        # Odd number of elements
        else:
            l = n // 2
            med = new_list[l]

        # Return the median
        return med
      
      
# Case Study 1        
s = Solution()
nums1 = [1,3]
nums1 = [2]
result = s.findMedianSortedArrays(nums1, nums2)
print(result) # expected result -> 2.00000
      
# Case Study 2        
s = Solution()
nums1 = [1,2]
nums1 = [3,4]
result = s.findMedianSortedArrays(nums1, nums2)
print(result) # expected result -> 2.50000

# Case Study 3        
s = Solution()
nums1 = [1,2,4,6]
nums1 = [3,5]
result = s.findMedianSortedArrays(nums1, nums2)
print(result) # expected result -> 3.50000
