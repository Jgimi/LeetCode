class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pattern = ''

        length = len(str2)

        while length > 0:
            shift = 0
            if str1.replace(str2[shift:length], "") == "" and str2.replace(str2[shift:length], "") == "":
                    pattern = str2[shift:length]
                    break
            while shift+length<len(str2)+1:
                if str1.replace(str2[shift:length], "") == "" and str2.replace(str2[shift:length], "") == "":
                    pattern = str2[shift:length]
                    break
                else:
                    shift+=1
            length-=1
        return pattern