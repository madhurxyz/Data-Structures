#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    #Best Case is Omega(n)
    #Worst Case is O(n)
    #Answer: Theta(n)
    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    #Best Case is Omega(1)
    #Worst Case is O(n)
    def contains(self, key):
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b.data[0] == key:
                return True
        return False

    #Best Case is Omega(1)
    #Worst Case is O(n)
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b.data[0] == key:
                return b.data[1]
        raise KeyError('Key is not present in the HashTable')

    def resize(self):
        old_buckets = self.buckets
        self.buckets = [LinkedList() for i in range(len(self.buckets)*2)]

        for bucket in self.buckets:
            for item in bucket:
                self.set(item.key, item.value)


    #Best Case is Omega(1)
    #Worst Case is O(n)
    def set(self, key, value):
        """Insert or update the given key with its associated value"""

        load_factor = self.length()/self.bucket_size

        if load_factor > 0.75:
            self.resize()

        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b.data[0] == key:
                entry = (b.data[0], value)
                b.data = entry
                return
        bucket.append((key, value))

    #Best Case is Omega(1)
    #Worst Case is O(n)
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for b in bucket:
            if b.data[0] == key:
                bucket.delete(b.data)
                return
        raise KeyError('Key is not present in the HashTable')

    #Best Case Omega(b + n)
    #Worst Case O(b + n)
    #Answer: Theta(b + n)
    def keys(self):
        """Return a list of all keys in this hash table"""
        keys = []
        for bucket in self.buckets:
            for b in bucket:
                if b is not None:
                    keys.append(b.data[0])
        return keys

    #Best Case Omega(b + n)
    #Worst Case O(b + n)
    #Answer: Theta(b + n )
    def values(self):
        """Return a list of all values in this hash table"""
        values = []
        for bucket in self.buckets:
            for b in bucket:
                if b is not None:
                    values.append(b.data[1])
        return values

    #Best Case Omega(1)
    #Worst Case O(1)
    #Answer: Theta(1)
    def __iter__(self):
        for bucket in self.buckets:
            if bucket:
                for b in bucket:
                    yield b
