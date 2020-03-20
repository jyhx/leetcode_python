#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        ret = ''
        for line in range(numRows):
            ret += ''.join([char for index,
                            char in enumerate(s) if (index+line) % (2*numRows-2) == 0 or (index-line) % (2*numRows-2) == 0])
        return ret
# @lc code=end
