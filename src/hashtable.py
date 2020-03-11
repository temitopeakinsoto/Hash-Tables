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
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0 


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        #start from an arbitrary prime number 
        hash_val = 9491 
        #iterate over each character in the key 
        for el in key: 
        #set hash value to the bit shift left by 5 
        #of the hash value and sum of the hash value
        #then add the value for the char
            hash_val = ((hash_val << 5) + hash_val) + ord(el)
        return hash_val


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
        hashe = self._hash_mod(key)
        if not self.storage[hashe]:
            self.storage[hashe] = LinkedPair(key, value)
        else:
            current_node = self.storage[hashe]
            while current_node:
                if current_node.key == key:
                    current_node.value = value 
                    return
                elif current_node.next:
                    current_node = current_node.next
                else:
                    break
            current_node.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print('Warning: key not found')
        else:
            self.storage[index] = None
        

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        hashe = self._hash_mod(key)
        if not self.storage[hashe]:
            return None
        current_node = self.storage[hashe]
        while current_node:
            if current_node.key == key:
                return current_node.value
            elif current_node.next:
                current_node = current_node.next
            else:
                return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        # double existing capacity
        self.capacity *= 2
        # copy existing storage
        new_store = list(self.storage)
        # create new array
        self.storage = [None] * self.capacity
        # go through all the items in the copied list removing none values
        for i in [item for item in new_store if item != None]:
          # set the current node to the current item
            current = i
            # if current node is not None
            while current is not None:
              # Insert into the New storage
              self.insert(current.key, current.value)
              # move to the next node
              current = current.next 


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
