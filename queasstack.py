class StackQueue:

  def __init__(self):
    self.val = None
    self.que = []
    self.d_q = []
  
  # No return Value
  def push(self,val):
    self.val = val
    self.que.append(self.val)

  # Removed
  def like_pop(self):

    # Pop ffrom Empty stack : 
    if len(self.que) == 0 :
      return('Pop from Empty Stack cant happen')
    i = 0
    # If length of queue is 1
    if len(self.que) == 1 : 
      return(self.que.pop())

    if len(self.d_q) == 0 :
      while(len(self.que)==1):
        self.d_q.append(self.que[i])
        self.que.remove(self.que[i])
        
    if len(self.d_q) == 0 : 
      ret_val = self.que.pop()
    # If pop is successfully done
    if len(self.que) == 0:
      for i in range(len(self.d_q)):
        self.que.append(self.d_q.remove(i))
    return(ret_val)

   # returns element
  def peek(self):
    return(self.que[0])



a = StackQueue()
a.push(1)
a.push(2)
a.push(3)
a.push(4)

print(a.que)
print(a.like_pop())
print(a.like_pop())
print(a.like_pop())
a.push(44)
print(a.like_pop())
print(a.like_pop())
