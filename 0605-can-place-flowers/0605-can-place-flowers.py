class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result = 0
        len_flo = len(flowerbed)
        

        for i in range(len_flo):
            if len_flo == 1 and flowerbed[i] == 0:
                result +=1
                break
            if i in [1,2] and flowerbed[0:2] == [0,0]:
                flowerbed[0:2] = [1,0]
                result +=1
            if i in [len_flo-2,len_flo] and flowerbed[-2:] == [0,0]:
                flowerbed[-2:] = [0, 1]
                result += 1
            else:
                if flowerbed[i-1:i+2] == [0,0,0]:
                    flowerbed[i - 1:i + 2] = [0, 1, 0]
                    result += 1

        
        return n<=result
                
                
        