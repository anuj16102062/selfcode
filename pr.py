def fun(n):
    r = 0
    for i in n:
        if len(str(i))%2 ==0:
            r +=1
    return print(r)
n = [25,55,879,1771]
fun(n)
