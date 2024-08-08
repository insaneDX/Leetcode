from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to target.
        
        Arguments:
        candidates : List[int] - List of candidate numbers.
        target : int - The target sum for the combinations.
        
        Returns:
        List[List[int]] - A list of all unique combinations that sum to the target.
        """
        path = []
        start = 0
        result = []
        return self.helper(candidates, target, path, start, result)

    def helper(self, candidates: List[int], target: int, path: List[int], start: int, result: List[List[int]]) -> List[List[int]]:
        """
        Helper function to perform backtracking to find all unique combinations.
        
        Arguments:
        candidates : List[int] - List of candidate numbers.
        target : int - The target sum for the combinations.
        path : List[int] - Current combination of numbers being explored.
        start : int - Index to start the exploration to ensure unique combinations.
        result : List[List[int]] - List to store all valid combinations.
        
        Returns:
        List[List[int]] - A list of all unique combinations that sum to the target.
        """
        if sum(path) == target:
            result.append(list(path))  # Append a copy of the current path to the result
            return
        if sum(path) > target:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])  # Choose the current candidate
            self.helper(candidates, target, path, i, result)  # Explore further with the current candidate
            path.pop()  # Un-choose the last candidate to backtrack
        
        return result
