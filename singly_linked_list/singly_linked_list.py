class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next = node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def set_tail(self, new_node):
        if not isinstance(new_node, Node):
            new_node = Node(new_node)

        if not self.tail:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None

        value = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return value

    def remove_tail(self):
        if not self.tail:
            return None

        value = self.tail.value

        if self.tail is self.head:
            self.head = None
            self.tail = None
        else:
            current_node = self.head

            while (current_node.next is not self.tail):
                current_node = current_node.next

            current_node.next = None

        return value

    def contains(self, value):
        if not self.head:
            return False

        current_node = self.head
        while (current_node is not None):
            if current_node.value == value:
                return True

            current_node = current_node.next

        return False

    def get_max(self):
        if not self.head:
            return None

        current_node = self.head
        current_max = current_node.value

        while (current_node is not None):
            current_max = max(current_max, current_node.value)
            current_node = current_node.next

        return current_max
