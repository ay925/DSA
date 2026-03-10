class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
# node1=Node(4)
# node2=Node(10)
# node3=Node(50)
# node4=Node(20)

# node1.next=node2
# node2.next=node3
# node3.next=node4



class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
        else:
            curr=self.head
            while(curr.next is not None):
                curr=curr.next
            curr.next=newNode

    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            curr= self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next

sll=SinglyLinkedList()
sll.append(5)
sll.append(10)
sll.append(15)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(80)
sll.append(1000)
sll.traversal()

