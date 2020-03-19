#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in num_to_index:
                return [num_to_index[another_num], index]
            num_to_index[num] = index
        return None
# @lc code=end

