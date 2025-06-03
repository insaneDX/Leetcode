class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        L = len(beginWord)
        all_pattern = defaultdict(list)

        # Build a map of wild card patterns for each word
        for word in wordList:
            for j in range(L):
                pattern = word[:j] + "*" + word[j+1:]
                all_pattern[pattern].append(word)
    
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()
            # Find nearest pattern of word
            for j in range(L):
                pattern = current_word[:j] + "*" + current_word[j+1:]
                for neighbor in all_pattern[pattern]:
                    if neighbor == endWord:
                         return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
        return 0



