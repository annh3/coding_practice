Example 1:

Input: 

       1
      / \
     2   3

Output: 6

Example 2:

Input: 

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''

"""
idea can you reduce this problem to maximum subarray sum?

in-order traversal of example 2 yields

[9, -10, 15, 20, 7]

Example 3:

   15
   / \
  -500  20
    /  \
   -500   7
   
[-500, 15, -500, 20, 7]
path we want: 15 -> 20 -> 7


property -> as long as i < j < k
then i -> j -> k is a valid path through the tree?
no -> example 2: 9, 15, 7

think recursively
LHS, vs RHS

lhs_sum
rhs_sum

golabalmax=max(globalmax, root + lhs_sum + rhs+sum, lhs_sum + root, lhs_sum, rhs_sum + root, rhs_sum)

define base cases
at a leaf node (you can check by checking "children"), return leaf value

return root.val+(left, right, 0)
