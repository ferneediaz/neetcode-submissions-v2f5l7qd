class Node:
    """
    A Node represents a single cache entry in our doubly linked list.
    
    WHY a doubly linked list?
    - We need to quickly move nodes around (remove from middle, insert at end).
    - A doubly linked list lets us do this in O(1) because each node knows
      both its predecessor AND successor.
    
    WHEN is this created?
    - Every time we call put() with a new key.
    - Every time we update an existing key in put().
    """
    def __init__(self, key, val):
        self.key = key      # The identifier (what the user gives us)
        self.val = val      # The data (what the user wants to retrieve)
        self.prev = None    # Pointer to the node on the LEFT (older)
        self.next = None    # Pointer to the node on the RIGHT (newer)


class LRUCache:
    """
    LRU Cache = Least Recently Used Cache
    
    WHAT does it do?
    - Stores key-value pairs like a dictionary.
    - When it gets full, it automatically removes the LEAST RECENTLY USED item.
    
    HOW does it work?
    - Dictionary (hash map): Gives us O(1) lookups by key.
    - Doubly Linked List: Tracks which items are old vs. new.
      * LEFT side = Least Recently Used (LRU) items
      * RIGHT side = Most Recently Used (MRU) items
    
    WHY this design?
    - We need both O(1) lookup AND O(1) removal of the oldest item.
    - A simple dictionary doesn't track "age" of items.
    - A simple linked list doesn't give us O(1) lookups.
    - Combined: We get the best of both worlds!
    """
    
    def __init__(self, capacity: int):
        """
        WHEN does this run?
        - Only once, when we create the cache object.
        
        WHAT are we doing?
        - Setting up the cache with a maximum size (capacity).
        - Creating two "dummy" nodes that act as boundaries.
        """
        self.cap = capacity
        
        # Dictionary to store: key -> Node object
        # WHY store the entire Node, not just the value?
        # - The Node has pointers (prev, next) so we can move it in the list.
        # - If we stored just the value (integer), we couldn't reorder it!
        self.cache = {}  # { key: Node_object }

        # Create two DUMMY nodes (boundary markers)
        # These are PERMANENT fixtures that never get deleted.
        self.left = Node(0, 0)   # LRU side (represents "oldest")
        self.right = Node(0, 0)  # MRU side (represents "newest")
        
        # Initialize the list as: [left] <-> [right] (empty, no real data yet)
        # WHY dummy nodes?
        # - Avoids checking "is the list empty?" or "is this the first node?"
        # - Every real node will always have a prev and next.
        # - Simplifies our remove/insert logic significantly!
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        """
        WHEN does this run?
        - In get() when we access a key (it becomes "recent" so move it).
        - In put() when we update an existing key.
        - In put() when we evict the LRU item due to capacity overflow.
        
        WHAT are we doing?
        - Removing a node from the middle of the linked list.
        - The node stays in memory, but it's no longer in the chain.
        
        HOW does it work (the magic of doubly linked lists)?
        - The node has pointers to its left neighbor (prev) and right neighbor (next).
        - We tell the left neighbor: "Your right neighbor is now my right neighbor."
        - We tell the right neighbor: "Your left neighbor is now my left neighbor."
        - This "stitches over" the node, removing it from the chain.
        
        WHY O(1)?
        - We don't search for anything. We just rearrange pointers.
        - No iteration, no loops.
        
        Visual Example:
        BEFORE:  [A] <-> [B] <-> [C] <-> [D]
        Remove B:
        - B.prev is A, B.next is C
        - Tell A: "your next is now C" (A.next = C)
        - Tell C: "your prev is now A" (C.prev = A)
        AFTER:   [A] <-> [C] <-> [D]
        """
        prev = node.prev  # The node to the LEFT of this node
        nxt = node.next   # The node to the RIGHT of this node
        
        # Stitch them together, skipping over 'node'
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        """
        WHEN does this run?
        - In put() when we add a new key to the cache.
        - In put() when we update an existing key (after removing the old version).
        - In get() when we access a key (moving it to "most recent").
        
        WHAT are we doing?
        - Adding a node to the RIGHT side of the linked list (the "most recent" end).
        - New/recently-accessed items go to the right.
        - This makes the list age from right (new) to left (old).
        
        HOW does it work?
        - We always insert RIGHT BEFORE the 'right' dummy node.
        - The position: [something] <-> [NEW NODE] <-> [right dummy]
        - This way, recently used items cluster near the right dummy.
        - Old, unused items drift toward the left dummy.
        
        WHY always at the right?
        - It marks the item as "just used" or "recently updated".
        - The item closest to self.left.next is the LRU (least recently used).
        
        Visual Example:
        Current state: [left] <-> [A] <-> [B] <-> [right]
        Insert C:
        - prev = self.right.prev = B
        - nxt = self.right
        - Connect: B <-> C <-> right
        New state:     [left] <-> [A] <-> [B] <-> [C] <-> [right]
        """
        # Find the current "last" node (most recent before we insert)
        prev = self.right.prev
        # The anchor on the right
        nxt = self.right
        
        # Create the chain: prev <-> node <-> nxt
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        """
        WHEN does this run?
        - User calls lru_cache.get(key) to retrieve a value.
        
        WHAT are we doing?
        - Looking up a key in the cache.
        - If found: return the value AND mark it as "recently used".
        - If not found: return -1.
        
        WHY mark it as recently used?
        - The user just accessed it, so it shouldn't be evicted soon.
        - We move it to the right (most recent) side of the list.
        
        Time Complexity: O(1)
        - Dictionary lookup: O(1)
        - Remove node from list: O(1)
        - Insert node to list: O(1)
        
        Example Walkthrough:
        Cache state: {1: Node1, 2: Node2, 3: Node3}
        List:        [left] <-> [Node2] <-> [Node1] <-> [Node3] <-> [right]
        
        Call: get(1)
        1. Is 1 in cache? Yes!
        2. Remove Node1 from its current spot.
           List becomes: [left] <-> [Node2] <-> [Node3] <-> [right]
        3. Insert Node1 at the right.
           List becomes: [left] <-> [Node2] <-> [Node3] <-> [Node1] <-> [right]
        4. Return Node1.val
        
        Now Node1 is marked as "recently used" because it's at the right.
        """
        if key in self.cache:
            # Key exists! Retrieve the Node object from the dictionary.
            # Remember: self.cache stores entire Node objects, not just values.
            
            # Step 1: Remove it from wherever it currently is in the list
            # WHY? Because we're about to mark it as "just used".
            self.remove(self.cache[key])
            
            # Step 2: Insert it at the right (most recent position)
            # This shows that we just accessed it.
            self.insert(self.cache[key])
            
            # Step 3: Return the value stored in this node
            return self.cache[key].val
        
        # Key doesn't exist in cache
        return -1

    def put(self, key: int, value: int) -> None:
        """
        WHEN does this run?
        - User calls lru_cache.put(key, value) to store or update a value.
        
        WHAT are we doing?
        - Adding a new key-value pair, OR
        - Updating an existing key's value.
        - Removing the least recently used item if we exceed capacity.
        
        Time Complexity: O(1)
        - Dictionary operations: O(1)
        - Linked list operations: O(1)
        - Finding LRU (self.left.next): O(1)
        
        This is the most complex operation. Let's break it down:
        
        SCENARIO 1: Key already exists
        ================================
        Cache: {1: Node1, 2: Node2}
        List:  [left] <-> [Node1] <-> [Node2] <-> [right]
        Call:  put(1, 99)  (updating key 1 with new value)
        
        1. Remove the old Node1 from the list
           List: [left] <-> [Node2] <-> [right]
        2. Create a NEW Node(1, 99) and add to cache and list
           self.cache[1] = Node(1, 99)
           self.insert(Node(1, 99))
           List: [left] <-> [Node2] <-> [Node(1, 99)] <-> [right]
        3. Check capacity: len(cache) = 2, cap = 2, OK!
        
        SCENARIO 2: New key (no overflow)
        ==================================
        Cache: {1: Node1}
        List:  [left] <-> [Node1] <-> [right]
        Call:  put(2, 20)  (capacity = 2)
        
        1. Key 2 doesn't exist, skip the removal.
        2. Create Node(2, 20) and add to cache and list
           self.cache[2] = Node(2, 20)
           self.insert(Node(2, 20))
           List: [left] <-> [Node1] <-> [Node(2, 20)] <-> [right]
        3. Check capacity: len(cache) = 2, cap = 2, OK!
        
        SCENARIO 3: New key (capacity exceeded - EVICTION!)
        ====================================================
        Cache: {1: Node1, 2: Node2}
        List:  [left] <-> [Node1] <-> [Node2] <-> [right]
        Call:  put(3, 30)  (capacity = 2)
        
        1. Key 3 doesn't exist, skip the removal.
        2. Create Node(3, 30) and add to cache and list
           self.cache[3] = Node(3, 30)
           self.insert(Node(3, 30))
           List: [left] <-> [Node1] <-> [Node2] <-> [Node(3, 30)] <-> [right]
           Cache: {1: Node1, 2: Node2, 3: Node(3, 30)}
        
        3. Check capacity: len(cache) = 3, cap = 2, OVERFLOW!
           
           a) Find the LRU node:
              lru_node = self.left.next  (which is Node1)
              
              Why self.left.next?
              - self.left is the dummy node on the LEFT.
              - self.left.next is the FIRST real node in the list.
              - This node is the OLDEST (closest to the LRU side).
              - It's the one we want to evict!
           
           b) Remove it from the list:
              self.remove(lru_node)
              List becomes: [left] <-> [Node2] <-> [Node(3, 30)] <-> [right]
           
           c) Delete it from the cache dictionary:
              del self.cache[1]
              Cache becomes: {2: Node2, 3: Node(3, 30)}
           
           Now we're back to capacity!
        """
        
        # STEP 1: Handle existing keys
        if key in self.cache:
            # The key already exists. Remove its old Node from the list.
            # WHY? Because we're about to update it and mark it as "recently used".
            self.remove(self.cache[key])
        
        # STEP 2: Add the new (or updated) key-value pair
        # This creates a brand new Node object.
        # If the key already existed, we replace the old Node with this new one.
        self.cache[key] = Node(key, value)
        
        # STEP 3: Insert the node at the RIGHT (most recent position)
        # This marks it as "just added" or "just updated".
        self.insert(self.cache[key])

        # STEP 4: Check if we exceeded capacity
        # If len(cache) > capacity, we need to evict the LRU item.
        if len(self.cache) > self.cap:
            # Find the LRU node (the one closest to self.left)
            # self.left.next is ALWAYS the first "real" node (the oldest one)
            lru_node = self.left.next
            
            # Remove it from the doubly linked list
            # After this, it's no longer in the chain.
            self.remove(lru_node)
            
            # Delete it from the dictionary completely.
            # Now it's gone from BOTH the list AND the cache.
            del self.cache[lru_node.key]
