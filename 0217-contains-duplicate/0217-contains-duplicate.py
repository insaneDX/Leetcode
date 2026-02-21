class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set() # num: occurances

        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        
        return False

# Time complexity: O(n)
# Space complexity: O(n)
        