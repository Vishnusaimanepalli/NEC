class LinkedList:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 10

    def get_size(self):
        return self.size

    def is_size_empty(self):
        return self.size == 0

    def first_node(self, data):
        node = self.Node(data)
        self.add_first_node(node)

    def add_first_node(self, node):
        if self.is_size_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node