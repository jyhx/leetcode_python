#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if i != len(nums)-1 and nums[i] == nums[i+1]:
                continue
            nums[ret] = nums[i]
            ret += 1
        return ret 
# @lc code=end

