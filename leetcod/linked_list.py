class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        
        
class LinkedList:
    def __init__(self, iterable):
        self.head = None
        prev = None
        for v in iterable:            
            n = Node(v)
            if prev == None :
                self.head = n
            else:
                prev.next = n
            prev = n
        
    def add(self, v):
        n = Node(v)
        n.next = self.head
        self.head = n
        
    def __str__(self):
        array = []
        h = self.head
        while h  :
            array.append(str(h.value))
            h = h.next
        return ", ".join(array)
    
    def reverse(self):
        prev =  None
        last = self.head
        while last:
            n = last            
            last = last.next            
            if prev == None :
                n.next = None                                
            else:
                n.next = prev  
            prev = n     
        self.head = prev
        return self
    
    def reverse_recusive(self):        
        def helper(head):
            if head == None:
                return (None, Node)           
            first_node =  head
            remaing_head, remaing_tail= helper(first_node.next)
            if remaing_head :
                first_node.next = None
                remaing_tail.next = first_node
                return (remaing_head, first_node)
            return (first_node, first_node)
            
        h, _ = helper(self.head)   
        self.head = h
        return self        
            
            
a = [1, 2, 3, 4]            
ll = LinkedList(a)
print(ll)
            
rll = ll.reverse()
print(rll)

rll = ll.reverse_recusive()
print(rll)