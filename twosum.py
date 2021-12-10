def twoSum(nums,target):
    h = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if h.get(diff)  is not None:
            return print([nums[h.get(diff)],nums[i]])
        else :
            h[nums[i]] = i
n = [7,1,3,8]
target = 9
twoSum(n,target)
