class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: o(n)
        # space: o(n)
        hashmap = {}
        for i in range(len(nums)):
        #curr + x = target or x = target - curr. Find X
            x = target - nums[i]
            if x in hashmap:
                return [hashmap[x], i]
            hashmap[nums[i]] = i # build hasmap

        return []