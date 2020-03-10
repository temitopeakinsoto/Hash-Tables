# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` storage
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of storage in the hash table
        self.storage = [None] * capacity
        self.count = 0 

  
    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        start = time.time()
        hash(key)
        end = time.time()
        return hash(key)
        


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
      #start from an arbitrary prime number 
      hash = 9491 
      #iterate over each character in the key 
      for el in key: 
        #set hash value to the bit shift left by 5 
        #of the hash value and sum of the hash value
        #then add the value for the char
        hash = ((hash << 5) + hash) + ord(el)
        #return the hash value
        return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
      


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        self.count += 1 
        #compute index of key using hash function
        index = self._hash(key)
        #create new node if bucket at index is empty 
        node = self.storage[index]        
        if node is None: 
          self.storage[index] = LinkedPair(key, value)
          return 
        
        prev = node 
        while node is not None: 
          #collision, a node exists at this index
          #iterate to the end of the list and add new node 
          #with provided  key / value 
          prev = node 
          node = node.next #iteration
          prev.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        #compute index of key using a hash function 
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None
        
        #iterate to the requested node 
        while node is not None and node.key != key: 
          prev = node
          node = node.next 
          
        if node is None:
          print("warning! key is not found")
        
        else: 
          self.count -= 1 
          result = node.value
          if prev is None:
            self.storage[index]  = node.next 
          else: 
            prev.next = prev.next.next
            
          return result


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None and node.key != key: 
          node = node.next 
        if node is None: 
          return None
        else: 
          return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        pass

    def __resize__(self):
      self.capacity *= 2
      new_storage = [None] * self.capacity
      for i in range(self.count):
         new_storage[i] = self.storage[i]
      self.storage = new_storage 
      



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
