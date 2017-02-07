from hashtable import HashTable

class Set(HashTable):
    def __init__(self, init_size=8):
          self.hash = HashTable()
          if iterable:
              for item in iterable:
                  self.add(item)

    def __repr__(self):
        return 'Set({})'.format(self.has.length())

    def length(self):
        return self.hash.length()

    def contains(self, item):
        return self.hash.contains(item)

    def add(self, item):
        if not self.hash.contains(item):
            self.hash.set(item, None)
            
    def remove(self,item):
        if not self.hash.contains(item):
            raise KeyError
        self.hash.delete(item)
        return item
