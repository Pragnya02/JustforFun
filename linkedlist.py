'''
Create Linked List
Traverse
Delete a value
Reverse
Traverse and print
print from kth to last index of linked list
@author : Pragnya Srinivasan
'''
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None 

class LinkedList:
  def __init__(self):
    self.head = None
    self.node = None
  
  def add_node(self,val):
    if self.head is None:
      self.head = Node(val)
      self.node = self.head
      
    else:
      new_node = Node(val)
      self.node.next = new_node
      self.node = new_node

  def print_list(self,k=None):
    curr = self.head
    temp=None
    i = 0
    if k :
      while curr:
        if i == k:
          temp = curr
        curr = curr.next
        i = i+1

    else:
      temp = self.head

    # if temp is None even if k is given , 
    # k is not within the len of linked list
    while temp:
      yield temp.data
      temp = temp.next

  def remove_node(self,val):
    temp = self.head  
    while temp:       
      if temp.data == val: 
        if not temp.next:
          #temp.data = None 
          self.head = None 
        else:
          temp.data = temp.next.data
          temp.next = temp.next.next
        return

      elif temp.next.data == val:
        temp.next = temp.next.next
        return
      else:
        temp = temp.next

  def reverse_ll(self):
    temp = self.head
    prev = None
    # Needs atleast 2 linked list elemets to reverse
    if not temp.next:
      return

    while temp:
      t_d = temp.next
      temp.next = prev
      prev = temp
      temp = t_d
    self.head = prev

  
llist = LinkedList()
llist.add_node(1)
#print(list(llist.print_list()))
llist.add_node(2)
print(list(llist.print_list()))
llist.add_node(3)
llist.add_node(4)
print(list(llist.print_list()))
llist.remove_node(2)
print(list(llist.print_list()))
llist.remove_node(1)
llist.remove_node(3)
llist.remove_node(4)
print(list(llist.print_list()))
llist.add_node(1)
llist.add_node(2)
llist.add_node(3)
llist.add_node(4)
llist.add_node(5)
llist.add_node(6)
print(list(llist.print_list()))
llist.reverse_ll()

print(list(llist.print_list()))

# Print from kth index to last
print(list(llist.print_list(3)))
