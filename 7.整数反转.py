#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        x, sign = (x, 1) if x > 0 else (-x, -1)
        while x != 0:
            ret *= 10
            ret += x % 10
            x //= 10
        return ret*sign if -2**31 <= ret*sign <= 2**31-1 else 0
# @lc code=end
