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

  def remove(self, value):
      # Start at the head
      current = self.head
      
      # Traverse to find the node with the value
      while current is not None:
          if current.data == value:
              # Case 1: Removing the only node
              if current == self.head and current == self.tail:
                  self.head = None
                  self.tail = None
              # Case 2: Removing the head
              elif current == self.head:
                  self.head = current.next
                  self.head.previous = None
              # Case 3: Removing the tail
              elif current == self.tail:
                  self.tail = current.previous
                  self.tail.next = None
              # Case 4: Removing a middle node
              else:
                  current.previous.next = current.next
                  current.next.previous = current.previous
              return  # Node found and removed
          
          current = current.next
    
    # If we get here, value was not found

  def update(self, item, value):
      # Start at the head
      current = self.head
      
      # Traverse the list to find the node with data == item
      while current is not None:
          if current.data == item:
              # Update the data with the new value
              current.data = value
              return  # Node found and updated
          
          current = current.next
      
      # If we get here, item was not found

  # TODO: find()
  def find(self, item):
    pass