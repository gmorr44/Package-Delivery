## The hashtable object is instaniated in the Packages.py file as the CSV data is read.
## All of the getter and setter methods are also implemented in the Packages.py file.


class HashTable:
    def __init__(self):
        self.size = 1
        self.map = [None] * self.size

    # creates a key to associate index position to package id.
    def get_hash(self,key):
        ##hash = 0
        hash = int(key) - 1
        return hash

    # adds the key value pair information that is read in from the CSV file.
    def add_package(self, key, value):
        key_hash = self.get_hash(key)
        key_value = [key, value]

        # The starting self.map size is 10. The following if statement appends another index location if the list is too small.
        if len(self.map) <= key_hash:
            self.map.append(None)
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        for pair in self.map[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.map[key_hash].append(key_value)
        return True

    # uses the package id as a key to directly access the package values.
    def get_package(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # access the specific key and removes the value from the hashtable.
    def delete_package(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
