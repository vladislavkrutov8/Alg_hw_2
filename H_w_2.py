# Alg_hw_2
Необходимо реализовать метод разворота связного списка (двухсвязного или односвязного на выбор).


class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		temp = None
		current = self.head
		while current is not None:
			temp = current.prev
			current.prev = current.next
			current.next = temp
			current = current.prev
		if temp is not None:
			self.head = temp.prev

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head is not None:
			self.head.prev = new_node
		self.head = new_node

	def printList(self, node):
		while(node is not None):
			print(node.data, end=' ')
			node = node.next


dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

dll.printList(dll.head)
print()

dll.reverse()

dll.printList(dll.head)
