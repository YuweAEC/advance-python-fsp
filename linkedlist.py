class Node:
    def __init__(self, info):
        self.__data = info
        self.__next = None
    def get_data(self):       # getter method
        return self.__data
    def set_data(self, info): # setter method
        self.__data = info
    def get_next(self):       # getter method
        return self.__next
    def set_next(self, next_node): # setter method
        self.__next = next_node
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
    def get_head(self):
        return self.__head
    def set_head(self, node):
        self.__head = node
    def get_tail(self):
        return self.__tail
    def set_tail(self, node):
        self.__tail = node
    def ll_append(self, info):
        # if the linked list does not pre-exist then create the linked list
        # otherwise append a new node at the end of the linked list
        new_node = Node(info)
        if (self.get_head() is None):
            new_node.set_next(None)
            self.set_head(new_node)
            self.set_tail(new_node)
            print ("Creating a linked list with a new node...")
        else:
            self.get_tail().set_next(new_node)
            self.set_tail(new_node)
            # print ("Appending the new node at the end of the linked list...")
    def ll_display(self):
        ptr = self.get_head()
        if (ptr == None):
            print ("Linked list is not pre-existing...")
        else:
            print ("Displaying the current content of the linked list...")
            while (ptr is not None):
                # print (f"Info = {ptr.get_data()} and link = {ptr.get_next()}...")
                print (ptr.get_data(), end = ", ")
                ptr = ptr.get_next()
        print ("\nEnd of the display operation...")
data_list = [33, 22, 11, 77, 55, 44, 66]
link_list = LinkedList()
for info in data_list:
    link_list.ll_append(info)
link_list.ll_display()