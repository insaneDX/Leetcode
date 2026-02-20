class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result_array = [0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result_array[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result_array[i] *= suffix
            suffix *= nums[i]

        return result_array




# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         prefix_array = [0]*len(nums)
#         prefix = 1
#         for i in range(len(nums)):
#             prefix_array[i] = prefix
#             prefix *= nums[i]
        
#         suffix_array = [0]*len(nums)
#         suffix = 1
#         for i in range(len(nums)-1, -1, -1):
#             suffix_array[i] = suffix
#             suffix *= nums[i]

#         result = [0]*len(nums)
#         for i in range(0,len(nums)):
#             result[i] = prefix_array[i]*suffix_array[i]

#         return result
# instead of maintaining prefix_array, suffix_array and then result we can combine everything into result itself while building