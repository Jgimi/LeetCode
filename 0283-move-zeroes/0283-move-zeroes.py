class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        check = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[check], nums[i] = nums[i], nums[check]
                check += 1
            else:
                continue
            
            