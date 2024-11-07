class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """A simple hash function using modulo operation"""
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Check if the key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Insert new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Key not found

    def delete(self, key):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True  # Key found and deleted
        return False  # Key not found

    def __repr__(self):
        """Representation of the hash table"""
        return "\n".join(f"{i}: {chain}" for i, chain in enumerate(self.table))

# Example usage
hash_table = HashTable(size=10)
hash_table.insert("apple", 1)
hash_table.insert("banana", 2)
hash_table.insert("grape", 3)

print("Hash Table after insertions:")
print(hash_table)

print("\nSearch for 'apple':", hash_table.search("apple"))
print("Delete 'banana':", hash_table.delete("banana"))
print("Hash Table after deletion:")
print(hash_table)
