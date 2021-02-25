import random
import operator
"""Find the k^th largest element in the array"""

def find_kth_largest(k, A):
	def find_kth(comp):
		# Partition A[left:right+1] around a pivot_idx
		# Returns the new index of the pivot after the partition

		# After partitioning, A[left:new_pivot_idx] contains elements
		# that are greater than or equal to the pivot, and A[new_pivot_idx+1:right+1]
		# contains elements that are less than the pivot

		# Note: "less than" is defined by the comp object

		def partition_around_pivot(left, right, pivot_idx):
			pivot_value = A[pivot_idx]
			new_pivot_idx = left

			A[pivot_idx], A[right] = A[right], A[pivot_idx]

			for i in range(left, right):
				if comp(A[i], pivot_value):

					A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]

					new_pivot_idx += 1

			A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]

			return new_pivot_idx

		left, right = 0, len(A)-1

		while left <= right:
			# Generate a random integer in [left, right]
			pivot_idx = random.randint(left,right)
			new_pivot_idx = partition_around_pivot(left, right, pivot_idx)

			if new_pivot_idx == k-1:
				return A[new_pivot_idx]
			elif new_pivot_idx > k-1:
				right = new_pivot_idx - 1
			else:
				left = new_pivot_idx + 1
	return find_kth(operator.gt)

if __name__ == "__main__":
	A = [random.randint(0,20) for _ in range(10)]
	print("A: ", A)
	k = 5
	res = find_kth_largest(k, A)
	print("res: ", res)