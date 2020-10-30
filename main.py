# This file will utilize and test my Linked List classes
from singly_linked_list import SinglyLinkedList

test_list = SinglyLinkedList()
# test append and prepend
test_list.append("SHINE")
test_list.prepend("Blinding Lights")
test_list.prepend("Yer Dad")
test_list.prepend("Self Destruct")
test_list.append("Dennis")
test_list.append("How Much a Dollar Cost")
test_list.print()

# test delete from head and tail
test_list.delete_from_head()
test_list.delete_from_tail()
test_list.print()

# test general delete
test_list.delete("SHINE")
test_list.print()

# test find
print(test_list.find("Dennis"))
print(test_list.find("Not in it"))
print("------------")

# test reverse
reversed_list = test_list.reverse()
reversed_list.print()
