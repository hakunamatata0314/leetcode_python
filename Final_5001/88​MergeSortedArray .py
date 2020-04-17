'''
(Leetcode ​88) ​Merge Sorted Array
Given two sorted integer arrays nums1 and nums2, 
merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal 
to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        # to modify nums1 in-place rather than create a new list
        # ans = [0] * p
        idx1, idx2 = m - 1, n - 1
        # use two pointers in nums1 and nums2 to compare the bigger num,
        # add the bigger num to the end of the nums1 instead of the beginning,
        # avoid changing nums at the front of nums1
        # quit the while loop when one of the pointers reach to the end
        while idx1 >= 0 and idx2 >= 0:
            if nums2[idx2] > nums1[idx1]:
                nums1[p] = nums2[idx2]
                idx2 -= 1
            else:
                nums1[p] = nums1[idx1]
                idx1 -= 1
            p -= 1
        # if the pointer of nums2 doesn't reach the end, means the numbers left in 
        # the uncompared part are all smaller than nums1, so add them to the front
        # you should increase pointer of nums1 by 1 and of nums by 1, respectively
        # if the pointer of nums1 doesn't reach the end, simply skip this step keeping
        # the original nums1 front part.
        if idx2 >= 0:
            nums1[:p+1] = nums2[:idx2+1]