#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                index = i - 1
                for j in range(len(nums)-1,index,-1):
                    if nums[j] > nums[index]:
                        nums[j],nums[index] = nums[index],nums[j]
                        nums[index+1:] =  nums[index+1:][::-1]
                        return
        nums[:] = nums[::-1]
        return        

# @lc code=end

