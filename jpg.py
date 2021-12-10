def fun(s):
    p =''
    c =0
    for i in range(len(s)):
        if s[i] == 'p':
            s.replace('p','')
            c+=1
        else:
            p +=s[i]
    print(p,c)
if __name__ == "__main__":
    s = 'sbpnmbvadmjbpnpc'
    fun(s)
    ###unique char in string
def fun(s):
    p =[]
    counts ={}
    for i in s:
        if i in counts:
            counts[i] +=1
        else:
            p.append(i)
            counts[i] = 1
    for i in p:
        if counts[i] == 1:
        
            print(i)## all non repeating char
if __name__ == "__main__":
    s = 'PythonforallPythonMustforall'
    fun(s)
    ##Program to find the index of first Recurring Character in the given string in Python
from collections import defaultdict
class Solution:
   def solve(self, s):
      chars = defaultdict(int)
      for i in range(len(s)):
         if s[i] in chars:
            return i
         else:
            chars[s[i]] += 1
      return -1
ob = Solution()
print(ob.solve("abcade"))
