# Node class represents each element (node) in the linked list
class Node:
    def __init__(self , data):
        self.data=data  # Stores the data
        self.next=None  # Points to the next node in the list

# LinkedList class to manage nodes and perform operations
class LinkedList:
    def __init__(self):
        self.head = None
    
    # Adds a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node        # If list is empty, new node becomes head
        else:
            current_node = self.head
            while current_node.next:
                current_node =current_node.next
            current_node.next=new_node    # Append the new node at the end

    # Prints the linked list
    def print_list(self):
        if self.head is None:
            return print("List is empty.")
    
        current_node = self.head
        # Traverse and print each node's data
        while current_node:
            print(current_node.data , end ="-->")
            current_node=current_node.next
        print("None")  # Indicate end of list

    # Deletes the nth node (1-based index)
    def delete(self , n):
        try:
            if self.head is None:
                raise IndexError("List is empty.Nothing to delete")
            
            if(n<=0):
                raise IndexError("Index cannot be less then 1 ")
            
            if(n==1):
                self.head=self.head.next
                return print("1st (head) node deleted ")
            
            
            current_node=self.head
            index=1
            while current_node and index<n-1:
                current_node=current_node.next
                index+=1
            
            # If position is invalid (too large)
            if current_node is None or current_node.next is None :
                raise IndexError("You are trying to delete a node that does not exist.")
            
            else :
                # Remove nth node by skipping it
                current_node.next=current_node.next.next
                return print(f"Node with Index {n} is deleted")
            
        except IndexError as e:
            print(f"Error: {e}")

# Test the implementation
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    print("Original list:")
    ll.print_list()

    print("\nDeleting -1th node:")
    ll.delete(-1)

    print("\nDeleting 2nd node:")
    ll.delete(2)
    ll.print_list()

    print("\nTrying to delete 10th node:")
    ll.delete(10)

    print("\nDeleting 1st node:")
    ll.delete(1)
    ll.print_list()

    print("\nDeleting Remaining nodes")
    ll.delete(1)
    ll.print_list()
    ll.delete(1)
    ll.print_list()

    print("\nAttempting to delete from empty list:")
    ll.delete(1)

    