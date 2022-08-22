# creating a linked list
# define class node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next #iterating through the linked list one by one

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    
    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self, index):
        if index <0 or index>self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index <0 or index>self.get_length():
            raise Exception("Invalid index")
            
        if index == 0: 
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next
            count += 1
    
    # Adding reversed linked list function using iterative method
    def reversedLL(self):
        if self.head is None:
            return 
        
        new = None
        itr = self.head
        while itr:
            hold = itr.next
            itr.next = new
            new = itr
            itr = hold
            
        self.head = new
    
        return 

if __name__ == '__main__':
    #pass
    ll = LinkedList()
    ll.print()
    '''
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(79)
    ll.insert_at_end(1)
    ll.insert_at_beginning(31)
    ll.insert_at_end(81)
    ll.print()
    print(ll.get_length())
    
    ll.insert_values(['a','b','c','d','e'])
    ll.print()
    ll.insert_at(0,'z')
    ll.insert_at(3, 'x')
    #ll.remove_at(2)
    #ll.remove_at(20)
    #ll.remove_at(0)
    #ll.remove_at(-1)
    
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.insert_at(1, 55)
    ll.print()
    '''
    ll.insert_values(['a','b','c','d','e'])
    ll.print()
    ll.reversedLL()
    ll.print()
   
    
