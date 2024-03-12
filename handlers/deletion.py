class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]
        slot = self.table[key_hash]

        for pair in slot:
            if pair[0] == key:
                pair[1] = value
                return True
        slot.append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        slot = self.table[key_hash]

        for pair in slot:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        slot = self.table[key_hash]

        for pair in slot:
            if pair[0] == key:
                slot.remove(pair)
                return True
        return False
