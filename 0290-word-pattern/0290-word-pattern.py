class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        word_dict = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
                                
        for c, w in zip(pattern, words):
            if c in pattern_dict and pattern_dict[c] != w:
                return False
            if w in word_dict and word_dict[w] != c:
                return False
            pattern_dict[c] = w
            word_dict[w] = c
        
        return True
        
        ''''for i,j in enumerate(pattern):
            if j not in test_dict:
                test_dict[j] = words[i]
            else:
                if test_dict[j] == words[i]:
                    continue
                else:
                    return False
        return True'''
        
                
        
            