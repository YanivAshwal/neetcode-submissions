class ListNode:
    #New node constructor
    def __init__(self,val, next_node=None):
        #setting the lists val to = the desrired val 
        self.val = val
        #setting up the pointer
        self.next = next_node 

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        #sets 'cur' to heads next ptr (second node)
        cur = self.head.next
        #counter var
        i = 0 
        #while cur still points to a valid node (ie not null)
        while cur: 
            #checks if the counter == desired index
            if i == index: 
                #if it is then return the value
                return cur.val
            #if not increment 1 
            i+=1
            #and set cur to the next node
            cur = cur.next
        return -1 #if list is empty or index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        
        

    def insertTail(self, val: int) -> None:
        #sets tails next ptr to new node
        self.tail.next = ListNode(val)
        #sets 'tail' to current tails next ptr
        self.tail= self.tail.next

    def remove(self, index: int) -> bool:
        i = 0 
        cur = self.head
        while i  < index and cur: 
            i += 1 
            cur = cur.next
        
        if cur and cur.next: 
            if cur.next == self.tail:
                self.tail = cur 
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        #set cur to the heads pointer (for traversal)
        cur = self.head.next
        #instanstiate an empty list 
        result = []
        #loop through as long as cur != null
        while cur: 
            #add curs val to result list 
            result.append(cur.val)
            #set cur to be the next node 
            cur = cur.next
        #returns the final list 
        return result
