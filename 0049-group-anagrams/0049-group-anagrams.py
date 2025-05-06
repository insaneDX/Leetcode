class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for word in strs:
            key = tuple(sorted(word))  # Convert sorted list to a tuple for using as key
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word] 

        return list(hashmap.values()) 