#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        ret = 0
        if not str:
            return ret

        if str[0] == '-':
            str, sign = str[1:], -1
        elif str[0] == '+':
            str, sign = str[1:], 1
        else:
            sign = 1

        for char in str:
            try:
                num = int(char)
                ret *= 10
                ret += num
            except:
                break
        return min(2**31-1, max(ret*sign, -2**31))
# @lc code=end
