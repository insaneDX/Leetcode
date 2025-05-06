class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26 # for a to z words

            for char in word:
                count[ord(char) - ord("a")] += 1 # to make in range(1 to 26)
            
            result[tuple(count)].append(word)
        
        return list(result.values())

# Total time complexity: O(n × k) where n is the no of string and k is the time of count operation performed on k characters of string
# Space Complexity: O(n × k)


# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hashmap = {}

#         for word in strs:
#             key = tuple(sorted(word))  # Convert sorted list to a tuple for using as key
#             if key in hashmap:
#                 hashmap[key].append(word)
#             else:
#                 hashmap[key] = [word] 

#         return list(hashmap.values()) 

# Time Complexity:O( m.nlogn ), where nlogn for sorting for m words.
# Space Compleity: O(m * n) where m = number of strings in the list, n = average length of each string