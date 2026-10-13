class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None


    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1

        self.size += 1

    def remove(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return

        cur = self.head
        while cur.next is not None and cur.next.val != val:
            cur = cur.next

        cur.next = cur.next.next

            
class Hashset:
    def __init__(self, capacity = 16, load_factor = 0.75):
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0 
        self.buckets = [Linked_list() for i in range(self.capacity)]
    
    def _hash(self, key):
        if isinstance(key, str):
            data = key.encode('utf-8')
        else:
            data = str(key).encode('utf-8')
        
        hash_val = 0x811c9dc5 
        for byte in data:
            hash_val ^= byte
            hash_val *= 0x01000193  
            hash_val &= 0xFFFFFFFF  
        
        return hash_val % self.capacity
    
    def _get_load_factor(self):
        return self.size / self.capacity
    
    def _get_bucket(self, key):
        idx = self._hash(key)
        bucket = self.buckets[idx]
        return bucket
    
    def __setitem__(self, key, value):
        head = self._get_bucket(key).head
    
    def __getitem__(self, key):
        head = self._get_bucket(key).head
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return False
    
    def remove(self, key):
        pass
    
    
