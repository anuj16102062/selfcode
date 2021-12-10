def freq(n,k):
    h = {}
    #n.sort()
    for i in range(len(n)):
        if n[i] in h :
            h[n[i]] += + 1
        else:
            h[n[i]] = 1
    a = [0] * (len(h))
    j = 0
    for i in h:
        a[j] = [i,h[i]]
        j+=1
    print(a)
    a = sorted(a,key = lambda x:x[0],reverse = True)
    a = sorted(a,key = lambda x :x[1],reverse = True)
    print(h)
    for i in range(k):
        print(a[i][0],end=" ")
n = [1,1,1,2,2,3]
k = 2
freq(n,k)
