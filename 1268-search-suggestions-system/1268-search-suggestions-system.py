class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        root = TrieNode()

        # Build Trie
        for product in products:
            node = root
            for char in product:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        # search
        result = []
        node = root

        for char in searchWord:
            if node and char in node.children:
                node = node.children[char]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])
            
        node = root
        def display_trie(node, char='', depth=0):
            # Indent based on depth to show hierarchy
            indent = "  " * depth
            print(f"{indent}[{char}] Suggestions: {node.suggestions}")
            
            # Recursively print children
            for next_char in sorted(node.children.keys()):
                display_trie(node.children[next_char], next_char, depth + 1)
        
        # display_trie(node)

        return result