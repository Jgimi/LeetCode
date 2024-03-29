class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        new_arr = []
        for i in range(len(arr)):
            if arr[i]!=0:
                new_arr.append(arr[i])
            else:
                new_arr.extend([0,0])
        ln_arr = len(arr)
        arr[:] = new_arr[:ln_arr]