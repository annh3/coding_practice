import collections
import pdb

class ListNode:
	def __init__(self, data=0, next_node=None, prev_node=None):
		self.data = data
		self.next = next_node
		self.prev = prev_node

def search_list(L, key):
	while L and L.data != key:
		L = L.next
	# If key was not present in the list, L will have become null
	return L

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0

	def traverse(self):
		print("Traversing")
		cur = self.head
		while cur:
			print("data: ", cur.data)
			cur = cur.next

	def traverse_backwards(self):
		print("Traversing backwards")
		cur = self.tail
		while cur:
			print("data: ", cur.data)
			cur = cur.prev

	# insert new_node after node
	def insert_after(self, node, new_node):
		if self.length == 0:
			# if new_node.data == 'b':
			# 	print("CHEESE")
			self.head = new_node
			self.tail = new_node
			self.length += 1
			return self.head

		# if node == self.tail:
		# 	#print("HELLO")
		# 	new_node.prev = self.tail.prev
		# 	self.tail.prev.next = new_node
		# 	self.tail = new_node
		# 	self.length += 1
		# 	return

		if node == self.head:
			# if new_node.data == 'b':
			print("CRACKERS")
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
			self.length += 1
			print("tail data: ", self.tail.data)
			return self.head

		# if new_node.data == 'b':
		# 	print("PASTA")

		new_node.next = node.next
		node.next.prev = new_node
		node.next = new_node
		new_node.prev = node
		self.length += 1
		return new_node
		# To-Do: edge cases - head and tail

	# delete this node
	def delete(self, node):
		#print("from delete, isbn: ", node.data)
		#pdb.set_trace()

		#if node == self.tail:
		self.tail = self.tail.prev
		self.tail.next = None
		#print("self tail data: ", self.tail.data)
		del node
		self.length -= 1
		return

		# if node == self.head:
		# 	self.head = node.next
		# 	del node
		# 	self.length -= 1
		# 	return 

		# node.prev.next = node.next
		# node.next.prev = node.prev
		# del node
		# self.length -= 1
		# return

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.ll = LinkedList()
		self.cache = collections.defaultdict()

	def lookup(self, isbn):
		# return price
		# update poisiton in queue
		if isbn in self.cache:
			res = self.cache[isbn][0]
			pointer = self.cache[isbn][1]

			if pointer != self.ll:
				cur_node_data = pointer.data # need a deep copy?
				self.ll.delete(pointer)
				new_node = ListNode(cur_node_data)
				self.ll.insert_after(self.ll.head, new_node)

			return res[0], pointer

		else:
			cur_node_data = isbn # need a deep copy?
			new_node = ListNode(cur_node_data)
			self.ll.insert_after(self.ll.head, new_node)
			return -1

		# instead of moving to back, move to front of queue
		# we'll delete from the front of the queue
		return -1

	def insert(self, isbn, price):
		print("Inserting: ", isbn)
		# insert into hash table

		# create node
		new_node = ListNode(isbn)
		res = self.lookup(isbn)
		self.cache[isbn] = (price, new_node)

		self.size += 1
		if self.size > self.capacity:
			self.cleanup()

		# call lookup
		return res # returns the price

	def delete(self, isbn): # separate from our cleanup
		# delete from hash table
		pointer = self.cache[isbn][1] # node to self this is a copy! not a true reference
		self.ll.delete(pointer)
		del self.cache[isbn]

	def cleanup(self):
		self.delete(self.ll.tail.data)
		self.size -= 1

def test():
	lru_cache = LRUCache(3)
	lru_cache.insert('a', 1)
	lru_cache.ll.traverse()
	lru_cache.ll.traverse_backwards()
	lru_cache.insert('b', 2)
	lru_cache.ll.traverse()
	lru_cache.ll.traverse_backwards()
	lru_cache.insert('c', 3)
	lru_cache.ll.traverse()
	lru_cache.ll.traverse_backwards()
	lru_cache.insert('d', 4)
	lru_cache.ll.traverse()
	lru_cache.ll.traverse_backwards()

if __name__ == "__main__":
	test()