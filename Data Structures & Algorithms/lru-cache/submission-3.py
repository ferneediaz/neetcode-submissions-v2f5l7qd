class Node:
    def __init__(self,key,val):
        self.key  = key
        self.val = val

        
        self.prev = None
        self.next = None




class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {}
        self.cache = {}

        self.left = Node(0, 0)  # LRU side
        self.right = Node(0, 0) # MRU side
        
        # Connect them to each other
        self.left.next = self.right
        self.right.prev = self.left
    
    
    #remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next, nxt.prev = nxt, prev
    
    #insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            #remove from the list and delete the lru from the hashMap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]







