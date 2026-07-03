class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addNode(self, newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode

    def deleteNode(self, delNode):
        Dprev = delNode.prev
        Dnext = delNode.next
        Dprev.next = Dnext
        Dnext.prev = Dprev

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.deleteNode(curr)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.m[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)