import collections

Interval = collections.namedtuple('Interval', ['left', 'right'])

def merge_intervals(listA, x):
	# add all the lists in listA that have right endpoint < x.left
	# merge all the lists which intersect x into x
	# add all the lists in listA which have left endpoint > x' right
	index = 0
	listB = []

	while index < len(listA) and listA[index].right <= x.left:
		listB.append(listA[index])
		index += 1

	while index < len(listA) and listA[index].left <= x.right:
		if listA[index].right > x.left:
			x.left = listA[index].left
		if listA[index].right > x.right:
			x.right = listA[index].right
		index += 1

	listB.append(x)

	while index < len(listA):
		listB.append(listA[index])
		index += 1

	return listB


