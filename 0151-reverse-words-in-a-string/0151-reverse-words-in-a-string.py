class Solution:
    def reverseWords(self, s: str) -> str:
        context_word = ''
        result = []
        for char in s:
            if char != ' ': 
                context_word += ''.join(char) # build context word
            else:                             # if space encountered then store context word
                if len(context_word)>0: 
                    result.append(context_word) 
                    context_word = '' # reset context word for next word build
                    
        if len(context_word) > 0:  # append last context word
            result.append(context_word)       
        
        return ' '.join(result[::-1])  # Reverse the list
        