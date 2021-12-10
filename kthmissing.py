def fun(num,k):
    l = 0
    r = len(num)-1
    while l <=r:
        m = (l+r)//2
        if num[m] -(m+1) < k:
            l = m+1
        else :
            r = m-1
    return print(l+k)
num = [1,2,8,9]
k =2
fun(num,k)
