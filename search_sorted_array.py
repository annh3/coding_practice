class Solution:
    def helper(self, nums: List[int], target: int, lh: int, rh: int) -> int:
        if lh > rh:
            return -1
        mid = (lh+rh) // 2
        if target == nums[mid]: 
            return mid
        if target == nums[lh]:
            return lh
        if target == nums[rh]:
            return rh
        
        # case 2.a, target > mid, lhs, rhs
        if target > nums[mid]:
            if target > nums[rh]:
                # Find the inflection point
                if nums[rh] < nums[mid]: # go right
                    return self.helper(nums, target, mid+1, rh)
                else:
                    return self.helper(nums, target, lh, mid-1)
            else:
                return self.helper(nums, target, mid+1, rh)
        else:
            # target <= nums[mid]
            if target < nums[lh]:
                # find the influection
                if nums[lh] > nums[mid]:
                    return self.helper(nums, target, lh, mid-1)
                else:
                    return self.helper(nums, target, mid+1, rh)
            else:
                return self.helper(nums, target, lh, mid-1)
        
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        res = self.helper(nums, target, 0, len(nums)-1)
        return res
