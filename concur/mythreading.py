import random
import time

import threading
from threading import Thread
"""
A simple example that demosntrates how threads work

We will subclass the Thread class and make it print
out its name to stdout
"""

class MyThread(threading.Thread):
	"""
	A threading example
	"""

	def __init__(self,name):
		"""
		Initialize the thread
		"""
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		"""
		Run the thread
		"""
		amount = random.randint(3,15)
		time.sleep(amount)
		msg = "%s is running" % self.name
		print(msg)

def create_threads():
	"""
	Create a group of threads
	"""
	for i in range(5):
		name = "Thread #%s" % (i+1)
		my_thread = MyThread(name)
		my_thread.start()

if __name__ == "__main__":
	create_threads()
