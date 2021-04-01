"""
By the pigeonhole principle, there must be at least one repeat

The question tells us to assume there is only one repeated number in nums

Note:
- Each integer is in the range [1,n] inclusive
- The index of the array goes from 0...to n (there are n+1 unique indices)

But there is no 1-1 mapping between values and indices
There exists some value in the array val = a[i] = a[j]

for i != j

Because each integer is in the range[1,n] we can intepret
an integer as an index without going out of bounds

The repeat value means that we will hit some index in the array
more than once the index is the value

b = [0]*(n+1)
"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        b = [0]*(len(nums)+1)
        for n in nums:
            if b[n] == 1:
                return n
            b[n] = 1
        return -1
