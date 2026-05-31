class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.hashmap = {}

        self.least = ListNode(0, 0)
        self.most = ListNode(-1, -1)

        self.least.next = self.most
        self.most.prev = self.least

    def remove(self, node):

        node.next.prev = node.prev
        node.prev.next = node.next

    
    def insert(self, node):

        node.next = self.most
        node.prev = self.most.prev

        node.prev.next = node
        self.most.prev = node


    def get(self, key: int) -> int:

        if key not in self.hashmap:
            return -1

        self.remove(self.hashmap[key])
        self.insert(self.hashmap[key])

        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:
            self.remove(self.hashmap[key])

            self.hashmap[key].val = value
            self.insert(self.hashmap[key])

            return

        if len(self.hashmap) == self.cap:
            
            del_key = self.least.next.key
            self.remove(self.least.next)

            del self.hashmap[del_key]

        self.hashmap[key] = ListNode(key, value)
        self.insert(self.hashmap[key])
            
