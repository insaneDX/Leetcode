class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0  # Pointer for the current position in the final list
        i = 0  # Pointer for the traversal of the input list
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            # Count the occurrences of the current character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            # Update the character in the final list
            chars[index] = char
            index += 1
            
            # If the count is greater than 1, update the count in the final list
            if count > 1:
                for digit in str(count):
                    chars[index] = digit
                    index += 1
        
        return index

# sol = Solution()
# chars = ["a", "a", "b", "b", "c", "c", "c"]
# length = sol.compress(chars)
# print(chars[:length])  # Output: ['a', '2', 'b', '2', 'c', '3']
