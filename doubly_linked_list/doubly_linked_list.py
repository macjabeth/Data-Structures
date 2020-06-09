"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        if not isinstance(value, ListNode):
            value = ListNode(value)
        current_next = self.next
        value.prev = self
        value.next = current_next
        self.next = value
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        if not isinstance(value, ListNode):
            value = ListNode(value)
        current_prev = self.prev
        value.prev = current_prev
        value.next = self
        self.prev = value
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if not isinstance(value, ListNode):
            value = ListNode(value, None, self.head)

        if not self.head:
            self.head = value
            self.tail = value
        else:
            self.head.insert_before(value)
            self.head = value

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        current_head = self.head
        self.delete(self.head)
        return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if not isinstance(value, ListNode):
            value = ListNode(value, self.tail)
        
        if not self.tail:
            self.tail = value
            self.head = value
        else:
            self.tail.insert_after(value)
            self.tail = value

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        current_tail = self.tail
        self.delete(self.tail)
        return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        node.next = self.head
        node.prev = None
        self.add_to_head(node)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
       self.delete(node)
       node.next = None
       node.prev = self.tail
       self.add_to_tail(node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev

        node.delete()

        self.length -= 1

        if self.length < 0:
            self.length = 0
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None

        node = self.head
        current_max = node.value

        while node is not None:
            current_max = max(current_max, node.value)
            node = node.next

        return current_max
