class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        array1 = [0] * 26
        array2 = [0] * 26

        for i in range(len(s1)):
            array1[ord(s1[i]) - ord('a')] += 1
            array2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if array1[i] == array2[i]:
                matches += 1
            
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            array2[index] += 1
            if array2[index] == array1[index]:
                matches += 1
            elif array2[index] - 1 == array1[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            array2[index] -= 1
            if array2[index] == array1[index]:
                matches += 1
            elif array2[index] + 1 == array1[index]:
                matches -= 1 

            l += 1
        
        return matches == 26

