class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums.sort(reverse=True)
        return nums
