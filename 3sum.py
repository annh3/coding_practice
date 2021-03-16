class Solution:
    def twoSum(self, target: int, numbers: List[int]) -> List[List[int]]:
        #print("target: ", target)
        #print("array: ", numbers)
        l = 0
        r = len(numbers)-1
        prev_1 = sys.maxsize
        ans = [[-1,-1]]
        while l < r:
            s = numbers[l] + numbers[r]
            if numbers[l] + numbers[r] == target and numbers[l] != prev_1:
                vals = [numbers[l], numbers[r]]
                #print("vals: ", vals)
                ans.append([l+1, r+1])
                prev_1 = numbers[l]
                l = l + 1
            elif s < target:
                l = l+1
            else:
                r = r-1
        return ans
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        #print("sorted nums: ", nums)
        if len(nums) < 3:
            return []
        res = []
        used_a = set()
        if len(nums) == 3 and nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] == 0 and nums[len(nums)-1] not in used_a:
            #print("hello")
            tmp = [nums[len(nums)-1],nums[len(nums)-2],nums[len(nums)-3]]
            #print("appending:, ", tmp)
            res.append([nums[len(nums)-1],nums[len(nums)-2],nums[len(nums)-3]])
        for i in range(len(nums)-3):
            target = nums[i]
            if target in used_a:
                continue
            used_a.add(target)
            cur = self.twoSum(-target, nums[i+1:])
            if len(cur) == 1:
                continue
            #print("i: ", i)
            #print("cur: ", cur)
            #print("array: ", nums)
            for c in cur[1:]:
                tmp = [target, nums[i+c[0]], nums[i+c[1]]]
                res.append(tmp)
        return res
