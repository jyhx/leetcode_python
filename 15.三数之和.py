#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for index, a in enumerate(nums):
            if index > 0 and a == nums[index-1]:
                continue
            left, right = index+1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] < -a:
                    left += 1
                elif nums[left] + nums[right] > -a:
                    right -= 1
                else:
                    ret.append([a, nums[left], nums[right]])
                    while left < right:
                        left += 1
                        if nums[left] != nums[left-1]:
                            break
                    while left < right:
                        right -= 1
                        if nums[right] != nums[right+1]:
                            break          
        return ret


# @lc code=end
