'''
219. 存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hasht = {}
        for i in range(len(nums)):
            if nums[i] not in hasht:
            	# 存下标
                hasht[nums[i]] = i
            else:
            	# 如果存在，就立刻返回 True
                if i - hasht[nums[i]] <= k:
                    return True
                else:
                    hasht[nums[i]] = i
        # 整个 nums 遍历完没有返回 True,才最终返回 False
        return False