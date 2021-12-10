def fun(n):
    s = 0
    e = len(n)-1
    while s < e:
        mid = (s+e)//2
        if n[mid] > n[mid+1]:
            e = mid
            # you are in deceasing part this may be ans but look at left 
        else:
            s = mid+1
            # you are in assen array 
    return print(s)## loop break when s == e that is the ans = 7
n = [1,3,5,7,4,2,0]
fun(n)
