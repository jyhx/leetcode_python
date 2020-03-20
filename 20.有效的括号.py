#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c in d and len(stack) != 0 and d[c] == stack.pop():
                pass
            else:
                return False
        return len(stack) == 0

# @lc code=end
