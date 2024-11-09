# linkedlist.py

class Node:
    def __init__(self, data, next=None):
        self.data = data  # Stores the value of the node
        self.next = next  # Points to the next node (None by default)


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with no nodes (empty list)

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the list
        new_node = Node(data, self.head)  # Set the new node's next to current head
        self.head = new_node  # Update the head to point to the new node

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        new_node = Node(data)
        if not self.head:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            probe = self.head
            while probe.next:  # Traverse until the last node
                probe = probe.next
            probe.next = new_node  # Set the last node's next to the new node

    def display(self):
        # Helper method to display the linked list
        nodes = []
        probe = self.head
        while probe:
            nodes.append(probe.data)
            probe = probe.next
        return " -> ".join(map(str, nodes)) if nodes else "Empty List"


# Testing the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()
    
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    
    print("Linked List:", ll.display()) 
