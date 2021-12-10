def fun(n,item):
    l = 0
    h = len(n) - 1
    mid = 0
    while l<=h:
        mid = (l + h)//2
        if n[mid] <item:
            l = mid+1
        elif n[mid]>item :
            h = mid-1
        else:
            return print(mid)
    return -1
fun([1,2,3,8,9,15],8)
def fun(n):
    p = []
    while n:
        min = n[0]
        for i in n:
            if i < min:
                min = i
        p.append(min)
        n.remove(min)
    print(p)
fun([19,9,5,99,87,95])
        


