# https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = -1
        r = len(nums)
        while l + 1 < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r