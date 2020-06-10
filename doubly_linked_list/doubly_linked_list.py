"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, nextN=None):
        self.value = value
        self.prev = prev
        self.next = nextN

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, prev=None, nextN=current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, prev=current_prev, nextN=None)
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
        # create a new node
        new_node = ListNode(value, None, None)

        # check if the DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        # check if the DLL is empty
        if self.head is None:
            return None
        # check if the DLL only has one node
        if self.length == 1:
            # get a reference of current head
            value = self.head.value
            # delete the head pointer
            self.head = None
            # delete the tail pointer
            self.tail = None
            self.length -= 1
            return value
        # otherwise get the current head reference
        value = self.head.value
        self.head.next.prev = None
        self.head = self.head.next
        self.length -= 1
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # create a new Node
        new_node = ListNode(value, None, None)
        self.length += 1
        # check if the DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list and add the new node to the tail
        else:
            # insert the new node after current tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # point the tail to the new node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.head is None:
            return None
        if self.length == 1:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        value = self.tail.value
        self.tail.delete()
        self.tail = self.tail.prev
        self.length -= 1
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if self.length > 1:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head.next = node.next
            self.head = node
        else:
            self.head = node
            self.tail = node

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is None:
            return
        if self.length > 1:
            oldTail = self.tail
            if node is not self.head:
                node.prev.next = node.next
            else:
                self.head = node.next
                self.head.prev = None

            node.prev = oldTail
            oldTail.next = node

            node.next = None
            self.tail = node
        else:
            self.head = node
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        max = 0
        if self.length:
            current = self.head
            max = current.value
        while current.next:
            if current.next.value > max:
                max = current.next.value
            current = current.next
        return max
