#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return None
        min_error = nums[0] + nums[1] + nums[2] - target
        nums.sort()
        for index, a in enumerate(nums):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                error = nums[right] + nums[left] - (target - a)
                if abs(min_error) > abs(error):
                    min_error = error
                if error > 0:
                    right -= 1
                elif error < 0:
                    left += 1
                else:
                    return target
        return target + min_error

# @lc code=end

