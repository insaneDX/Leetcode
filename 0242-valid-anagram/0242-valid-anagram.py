class Solution:
    def helper(self,hashmap, target):
        for char in target:
            if char in hashmap and hashmap[char] != 0:
                hashmap[char] -= 1
            elif char in hashmap and hashmap[char] < 0:
                return False
            else:
                return False
        for count in hashmap.values():
            if count != 0:
                return False
        return True
        
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
  
        return self.helper(hashmap, t)

        