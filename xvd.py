def fun(n):
    fm = n[0]
    sm = n[0]
    for i in range(1,len(n)):
        if n[i] > fm:
            fm = n[i]
    for i in range(1,len(n)):
        if n[i] > sm and fm != n[i]:
            sm = n[i]
    print(sm)
if __name__ == "__main__":
    n = [1,2,9,10,8,96]
    fun(n)
def fun(n):
    r = 0
    while n > 0:
        d = n %10
        r = r*10 +d
        n = n //10
    print(r)
if __name__ == "__main__":
    n = 105
    fun(n)
def fun(n):
    s = n[::-1]
    print(s)
if __name__ == "__main__":
    n = 105
    p = str(n)
    fun(p)
def fun(n):
    for i in  range(n,-1,-1):
        for j in range(i,-1,-1):
            print(j)
        print(' ')
if __name__ == "__main__":
    n = 5
    fun(n)
def fun(n,item):
    for i in range(len(n)):
        if n[i] == item :
            print(i)
    
if __name__ == "__main__":
    n = [1,2,9,10,8,96]
    fun(n,10)
def fun (s1,s2):

    c = 0
    for i in s1:
        for j in s2:
            if i ==j:
                c +=1 
                
    if c == len(s1):
        print('true')
if __name__ == "__main__":
    s1 = 'fun'
    s2 = 'nuf'
    fun(s1,s2)
    

