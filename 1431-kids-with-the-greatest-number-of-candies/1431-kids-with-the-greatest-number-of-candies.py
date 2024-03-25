class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        result = []

        for i in range(len(candies)):
            result.append(True if candies[i] >= max_val-extraCandies else False)
            
        return result
