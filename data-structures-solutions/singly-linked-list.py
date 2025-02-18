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
            
            
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        if self.head is None:
            return
    
        if self.head.data == data_after:
            node = Node(data_to_insert,self.head.next)
            self.head.next = node
            
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self, word):
    # Remove first node that contains data
        if self.head is None:
            return
        
        if self.head.data == word:
            self.head = self.head.next
               
        itr = self.head
        while itr.next:
            if itr.next.data == word:
                itr.next = itr.next.next
                break
            itr = itr.next
            

if __name__ == '__main__':
    #pass
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    
