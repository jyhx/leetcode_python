#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    if nums[left] + nums[right] < target - nums[i] - nums[j]:
                        left += 1
                    elif nums[left] + nums[right] > target - nums[i] - nums[j]:
                        right -= 1
                    else:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
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

