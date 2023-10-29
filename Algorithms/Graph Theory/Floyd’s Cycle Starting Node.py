class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
  
head = None
  
def detectLoop(head):
    slowPointer = head
    fastPointer = head
  
    while (slowPointer != None
           and fastPointer != None
           and fastPointer.next != None):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if (slowPointer == fastPointer):
            break
 
    if (slowPointer != fastPointer):
            return None
     
    slowPointer = head
    while (slowPointer != fastPointer):
      slowPointer = slowPointer.next
      fastPointer = fastPointer.next
    return slowPointer
   
  
head = Node(50)
head.next = Node(40)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(10)
  
temp = head
while (temp.next != None):
    temp = temp.next

temp.next = head
loopStart = detectLoop(head)

if (loopStart == None):
    print("Loop does not exists")
else:
    print(f"Loop does exists and starts from {loopStart.data}")