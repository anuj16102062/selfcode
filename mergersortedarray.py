def merge(nums1,m,nums2,n):
    po = len(nums1)-1
    m = m-1
    n = n-1
    while m>=0 and n >=0:
        if nums1[m] >= nums2[n]:
            nums1[po] = nums1[m]
            m-=1
        else:
            nums1[po] = nums2[n]
            n-=1
        po-=1
    if n>=0:
        nums1[:n+1] = nums2[:n+1]
    return print(nums1)
nums1 =[3,4,6,0,0]
m=3
n=2
nums2 = [1,5]
merge(nums1,m,nums2,n)
def twoSum(numbers,target):
    h = {}
    for i in range(len(numbers)):
        diff = target-numbers[i]
        print(diff)
        if h.get(diff) is not None:
            return  print([h.get(diff)+1,i+1])
        else:
            h[numbers[i]] = i
            print(h)
numbers = [2,3,4,5,6,7,8,9]
target = 9
twoSum(numbers,target)
    
