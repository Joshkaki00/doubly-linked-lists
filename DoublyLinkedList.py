from Node import Node

class DoublyLinkedList:
  
  def __init__(self):
    self.head = None
    self.tail = None

  # TODO: append()
  #Add to the end of the linked list
  def append(self, new_data):
    if self.head is None:#empty linked list
      new_node = Node(new_data)
      self.head = new_node
      self.tail = new_node
    else:
      #create a new node
      new_node = Node(new_data)
      #set new node previous to tail
      new_node.previous = self.tail
      #set tail.next to new node
      self.tail.next = new_node
      #move tail to new node
      self.tail = new_node

def insert(self, item, index):
    # Create the new node
    new_node = Node(item)
    
    # Case 1: Insert at the beginning (index 0)
    if index == 0:
        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # List has elements
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        return
    
    # Case 2: Insert at any other position
    # Traverse to the node at (index - 1)
    current = self.head
    position = 0
    
    while current is not None and position < index - 1:
        current = current.next
        position += 1
    
    # If current is None, index is out of bounds
    if current is None:
        return
    
    # Insert between current and current.next
    new_node.next = current.next
    new_node.previous = current
    
    if current.next is not None:  # Not inserting at the end
        current.next.previous = new_node
    else:  # Inserting at the end
        self.tail = new_node
    
    current.next = new_node

  # TODO: remove()
  def remove(self, value):
    pass

  # TODO: update()
  #Find and existing node with data == item and update with new value
  #traverse to find node
  #replace the data with value
  #hint: look at find() for singly linked list
  def update(self, item, value):
    pass

  # TODO: find()
  def find(self, item):
    pass