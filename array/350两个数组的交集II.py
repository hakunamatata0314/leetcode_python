'''
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	# 要先把短的list作为base
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        map1 = {}
        # 用dict里的get方法，或者if判断
        for n in nums1:
            map1[n] = map1.get(n, 0) + 1
        res = []
        for n in nums2:
        	# 这里一定要用get，如果nums2的元素不在nums1，会报index超标的错误
            if map1.get(n, 0) > 0:
                res.append(n)
                map1[n] -= 1
        return res