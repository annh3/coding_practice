def partition(A,l,h):
	i = l - 1 # this pointer is used to keep an index on the last place we've swapped to
	p_val = A[h]
	for j in range(l,h): # note we need to "look at" A[h] at the end
		if A[j] <= p_val:
			i += 1 # this is because we need to shift the block that is less than pivot
			# j will always be running ahead of i
			# if A[j] > p_val we skip this part, and just increment j
			tmp = A[i]
			A[i] = A[j]
			A[j] = tmp
	# we need to do the last variable
	i += 1
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp
	return i  # return pivot value


def quicksort(A,l,h):
	if l < h: # condition for valid pointers, otherwise we terminate divide-and-conquer
		pivot = partition(A,l,h)
		quicksort(A,l,pivot-1)
		quicksort(A,pivot+1,h)

def merge_sort(A,l,h):
	if l >= h:
		return

	mid = (l + h) // 2
	lhs = merge_sort(A,l,mid)
	rhs = merge_sort(A,mid+1,h)

	# merge
	new_array = [0]*len(A)
	i = 0
	r = mid+1
	while l < len(lhs) and r < len(rhs):
		if lhs[l] <= rhs[r]:
			new_array[i] = lhs[l]
			l += 1
			i += 1
		else:
			new_array[i] = rhs[r]
			r += 1
			i += 1

	if l < len(lhs):
		for k in range(l,len(lhs)):
			new_array[i] = lhs[k]
			i += 1
	if r < len(rhs):
		for k in range(r,len(rhs)):
			new_array[i] = rhs[k]
			i += 1

	return new_array


def max_middle_subarray(A,l,mid,h):
	# anchor at mid
	lsum = -1000000
	cursum = 0
	left_idx = mid

	for i in range(mid,l): # does this work?
		cursum += A[i]
		if cursum >= lsum:
			lsum = cursum
			left_idx = i

	rsum = -1000000
	cursum = 0
	right_idx = mid+1

	for i in range(mid+1,h):
		cursum += A[i]
		if cursum >= rsum:
			rsum = cursum
			right_idx = i

	return (left_idx, right_idx, lsum + rsum)


"""
This function returns the contiguous segment of the array 
which has the largest total sum of elements

returns: (l_idx, r_idx, val_of_sum)
"""
def max_subarray(A,l,h):
	if l == h:
		print("l: ", l, " h: ", h, " array len: ", len(A))
		return (l,h, A[l])

	mid = (l + h) // 2
	(ll, lh, lsum) = max_subarray(A,l,mid)
	(rl, rh, rsum) = max_subarray(A,mid+1,h)
	(ml, mh, msum) = max_middle_subarray(A,l,mid,h)

	if lsum >= rsum and lsum >= msum:
		return ll, lh, lsum
	elif rsum >= lsum and rsum >= msum:
		return rl, rh, rsum
	else:
		return ml, mh, msum




def test_1():
	array = [-1,0,3,7,9,2,4]

def test_subarray():
	# idx 7-10 with sum 43
	array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
	return array


if __name__ == "__main__":
	array = test_subarray()
	lval, rval, sumval = max_subarray(array, 0, len(array)-1)
	print(lval, rval, sumval)