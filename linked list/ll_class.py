class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Inserts a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        """Inserts a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Deletes the first occurrence of the specified key."""
        current = self.head
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current is None:
            print("Key not found.")
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Deleted {key}")

    def display(self):
        """Displays the list."""
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # Output: 10 -> 20 -> 30 -> None

ll.insert_at_beginning(5)
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

ll.delete(10)
ll.display()  # Output: 5 -> 25 -> 30 -> None
