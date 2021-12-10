import sys
def stockbuy(arr):
    mini = sys.maxsize
    profit = 0
    for i in range(len(arr)):
        if mini > arr[i]:
            mini = arr[i]
        elif  profit < (arr[i] - mini):
            profit = (arr[i] - mini)
    return print(profit)
arr = [7,1,5,3,6]
stockbuy(arr)
# this function return max profit 
def stockbuy(arr):
    diff = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            print('buy at ',i-1,'day','sell', 'at',i,'day')
            diff+=arr[i] - arr[i-1]
    return print(diff)
arr = [7,1,5,3,6]
stockbuy(arr)
def patter(txt,pat):
    n = len(txt)
    m = len(pat)
    for i in range(n-m+1):
        j = 0
        while j < m:
            if txt[i+j] != pat[j]:
                break  
            j+=1
        if j==m:
            print(i,'amtxhindex')
txt = 'thisopistextop'
pat = 'op'
patter(txt,pat)
def twosum(n,target):
    h = {}
    for i in range(len(n)):
        diff = target-n[i]
        if h.get(diff) is not None:
            print(h.get(diff),i)
        else:
            h[n[i]] = i
n = [1,8,5,9]
target = 10
twosum(n,target)
            

