#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) <= 0:
            return []
        d = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':''}
        if len(digits) == 1:
            return [s for s in d[digits[0]]]
        ret = []
        for char in d[digits[0]]:
            ret += [char+string for string in self.letterCombinations(digits[1:])]
        return ret
# @lc code=end

