#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ret = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[ret] = nums[i]
            ret += 1
        return ret

# @lc code=end
