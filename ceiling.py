def fun(n,target):
    l = 0
    h = len(n)-1
    while l<=h:
        mid = (l+h)//2
        if n[mid] > target:
            h = mid -1
        elif n[mid] <target:
            l = mid +1
        else:
            return print(n[mid])
    return print(n[l]) # for flour return n[h]
n = [1,2,5,9,14,16]
target = 10
fun(n,target)
#this is code for find next letter in array and if not in array return first element
def fun(n,target):
    l = 0
    h = len(n)-1
    while l<=h:
        mid = (l+h)//2
        if ord(n[mid]) > ord(target):
            h = mid -1
        else :
            
            l = mid +1
    return print(n[l%len(n)]) #yahan find karna hai target se bda aur array me smallest ho
m = ['a','d','f','i','p','s','t']
target1 = 'z'# 'p'
fun(m,target1)
