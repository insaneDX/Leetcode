class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
    
        def decode_ways(index: int) -> int:
            # If we've reached the end of the string, there's one way to decode it
            if index == len(s):
                return 1
        
            # If the string starts with a '0', no valid encoding exists
            if s[index] == '0':
                return 0
        
            # If this subproblem has already been solved, return the cached result
            if index in memo:
                return memo[index]
        
            # Decode single digit
            count = decode_ways(index + 1)
        
            # Decode two digits if valid
            if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                count += decode_ways(index + 2)
        
            # Cache the result
            memo[index] = count
        
            return count
    
        return decode_ways(0)