from random import randint
from threading import Thread, Lock

chopsticks = [Lock() for _ in range(5)]   # 5 chopsticks

def eat(i):

	first, last = min(i, (i+1) % 5), max(i, (i+1) % 5) # clever

	while True:
		print(("Philosopher %d waits for first chopstick" % i))
		with chopsticks[first]:
			print(("Philosopher %d waits for first chopstick" % i))
			with chopsticks[last]:
				sleep(randint(0,2)) # EAT

threads = [Thread(target=eat, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

