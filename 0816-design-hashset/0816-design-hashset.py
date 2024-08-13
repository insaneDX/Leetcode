class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        # Initialize the array with 10 buckets
        self.array = [[None, None] for _ in range(10)]

    def hashfunction(self, key):
        # Compute the hash value based on the key
        return key % 10

    def add(self, key: int) -> None:
        # Get the index for the key
        hash_index = self.hashfunction(key)
        if self.array[hash_index][0] == key:  # If the key is already in the array
            return
        # Check if there's no element at the hash index
        if self.array[hash_index][0] is None:
            self.array[hash_index][0] = key
        else:
            # Collision occurred
            if self.array[hash_index][1] is None:
                # Create a linked list at this index
                node = Node(key)
                self.array[hash_index][1] = node
            else:
                # Traverse the linked list to add the new node
                curr = self.array[hash_index][1]
                while curr.next:
                    if curr.val == key:
                        return  # Key already exists, no need to add
                    curr = curr.next
                if curr.val == key:
                    return  # Key already exists, no need to add
                curr.next = Node(key)

    def remove(self, key: int) -> None:
        # Get the index for the key
        hash_index = self.hashfunction(key)
        # Handle removal
        if self.array[hash_index][0] == key:
            if self.array[hash_index][1] is None:
                self.array[hash_index][0] = None
            else:
                # Remove key and adjust linked list
                curr = self.array[hash_index][1]
                self.array[hash_index][0] = curr.val
                if curr.next:
                    self.array[hash_index][1] = curr.next
                else:
                    self.array[hash_index][1] = None
        else:
            # Traverse linked list to find and remove the key
            curr = self.array[hash_index][1]
            prev = None
            while curr:
                if curr.val == key:
                    if prev:
                        prev.next = curr.next
                    else:
                        self.array[hash_index][1] = curr.next
                    return
                prev = curr
                curr = curr.next

    def contains(self, key: int) -> bool:
        # Get the index for the key
        hash_index = self.hashfunction(key)
        if self.array[hash_index][0] == key:
            return True
        elif self.array[hash_index][1] is not None:
            # Traverse the linked list to find the key
            curr = self.array[hash_index][1]
            while curr:
                if curr.val == key:
                    return True
                curr = curr.next
        return False

    def display(self):
        for i in range(len(self.array)):
            if self.array[i][0] is not None:
                print(f"Index {i}: {self.array[i][0]}", end="")
            if self.array[i][1] is not None:
                curr = self.array[i][1]
                while curr:
                    print(f" --> {curr.val}", end="")
                    curr = curr.next
                print(" --> None")
            else:
                print(" --> None")
