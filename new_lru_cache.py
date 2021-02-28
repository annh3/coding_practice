import collections
import pdb

class ListNode:
	def __init__(self, data=None, next_node=None, prev_node=None):
		self.data = data
		self.next = next_node
		self.prev = prev_node

def search_list(L, key):
	while L and L.data != key:
		L = L.next
	return L


class LinkedList:
	def __init__(self):
		self.head = ListNode()
		self.tail = ListNode()
		self.head.next = self.tail
		self.tail.prev = self.head
		self.length = 0

	def traverse(self):
		cur = self.head.next
		while cur:
			print("data: ", cur.data)
			cur = cur.next

	def traverse_backwards(self):
		cur = self.tail.prev
		while cur:
			print("data: ", cur.data)
			cur = cur.prev

	# delete this node! we can do pointers with is
	# the dummy variables help us out
	def delete(self, node):
		# prev's next should but node's next
		# next's prev should be node's prev

		node.prev.next = node.next
		node.next.prev = node.prev
		del node
		self.length -= 1

	# insert new node after node
	def insert_after(self, node, new_node):
		tmp = node.next
		node.next = new_node
		new_node.prev = node
		new_node.next = tmp
		tmp.prev = new_node

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

	def cleanup(self):
		isbn = self.ll.tail.prev.data
		self.ll.delete(self.ll.tail.prev)
		del self.cache[isbn]
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