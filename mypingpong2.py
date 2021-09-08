import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

class TaskEvenOdd(threading.Thread):

	def __init__(self, intmax, isEven, lock):
		super(TaskEvenOdd, self).__init__()
		self.intmax = intmax
		self.isEven = isEven
		self.lock = lock
		print("initialized taskevenodd")

	def run(self):
		print("starting thread")

		# initialize number
		if self.isEven:
			number = 2
		else:
			number = 1

		while number <= self.intmax:
			print("in the while loop and number is: ", number)
			time.sleep(0.5)
			acquired = self.lock.acquire(0)
			try:
				if acquired:
					logging.debug('Acquired by '+str(self.isEven))
					print("Printing: ", number)
					number += 2
			finally:
				if acquired:
					self.lock.release()




if __name__ == "__main__":
	lock = threading.Lock()
	t1 = TaskEvenOdd(10,False,lock)
	t2 = TaskEvenOdd(10,True,lock)
	t1.start()
	t2.start()
