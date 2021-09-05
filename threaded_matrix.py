from threading import Thread
import numpy as np
import pdb

def thread_function(v1,v2,C,i,j):
	ab = [v1[i]*v2[i] for i in range(len(v1))]
	ab = sum(ab)
	#pdb.set_trace()
	C[i][j] = ab

def multiply(A,B):
	n = len(A)
	C = [[0]*n for _ in range(n)]

	threads_list = { (i*n+j): None for j in range(n) for i in range(n)}
	print(threads_list)
	for i in range(n):
		for j in range(n):
			# C_i,j
			# Vector Vector produc
			idx = i*n + j
			t = Thread(target=thread_function,args=(A[i,:], B[:,j], C, i, j))
			threads_list[idx] = t
			t.start()

	for k, v in threads_list.items():
		#pdb.set_trace()
		v.join()

	return C

def test():
	A = np.array([[1,0],[0,1]])
	B = np.array([[1,0],[0,1]])
	C = multiply(A,B)
	print("C: ", C)

if __name__ == "__main__":
	test()
