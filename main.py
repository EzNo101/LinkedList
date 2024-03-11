from linked_list import LinkedList

my_list = LinkedList()

my_list.append(2)
my_list.append(4)
my_list.append(8)
my_list.append(16)

my_list.reverse()

print(my_list.tail.get_data())
my_list.show()