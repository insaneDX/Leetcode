class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        def search_binary(left, right):
            if left == right: # Base case where left and right both approach same element
                return nums[left]
            
            mid = (left + right)//2

            if nums[mid] > nums[right]:
                # Minimum is on the right half
                return search_binary(mid+1, right)
            elif nums[mid] < nums[right]:
                # Minimu is on the left hald
                return search_binary(left, mid)
            else:
                # if nums[mid] == nums[right], cant decide so search both branches
                return min(search_binary(left, mid), search_binary(mid+1, right))
        
        return search_binary(left, right)
                


                    

        