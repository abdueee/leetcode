class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        
        left = 0
        right = len(s) - 1
        
        while left<right:
            while left < right and s[left] not in vowels:
                left +=1
            while  left<right and s[right] not in vowels:
                right -= 1
            if left<right:
                temp = s[left]
                s[left]= s[right]
                s[right] = temp
            left += 1
            right -= 1
        
        return ''.join(s)
                