import numpy as np

def mergelists(listA, listB):
	ptr1 = 0
	ptr2 = 0
	collection = set()

	while(True):
		while ptr1 < len(listA) and ptr2 < len(listB) and listA[ptr1] < listB[ptr2]:
			ptr1 += 1

		if ptr1 == len(listA) or ptr2 == len(listB):
			return sorted(list(collection))

		while ptr1 < len(listA) and ptr2 < len(listB) and listA[ptr1] == listB[ptr2]:
			collection.add(listA[ptr1])
			ptr1 += 1
			ptr2 += 1

		if ptr1 == len(listA) or ptr2 == len(listB):
			return sorted(list(collection))

		while ptr1 < len(listA) and ptr2 < len(listB) and listA[ptr1] > listB[ptr2]:
			ptr2 += 1

		if ptr1 == len(listA) or ptr2 == len(listB):
			return sorted(list(collection))

		while ptr1 < len(listA) and ptr2 < len(listB) and listA[ptr1] == listB[ptr2]:
			collection.add(listA[ptr1])
			ptr1 += 1
			ptr2 += 1

		if ptr1 == len(listA) or ptr2 == len(listB):
			return sorted(list(collection))

	return sorted(list(collection))

def test1():
	listA = np.random.randint(low=0, high=10, size=5)
	listB = np.random.randint(low=0, high=10, size=8)

def test2():
	listA = [2,3,3,5,5,6,7,7,8,12]
	listB = [5,5,6,8,8,9,10,10]
	res = mergelists(listA, listB)
	print(res)

if __name__ == "__main__":
	test2()
	