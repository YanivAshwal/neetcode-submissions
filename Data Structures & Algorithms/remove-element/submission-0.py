class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val = 0
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = 1000
            else:
                not_val += 1
        nums.sort()

        return not_val
