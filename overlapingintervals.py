class solution:
    def over(self,n)->int:
        if not n:
            return 0
        n.sort(key = lambda x: x[0])
        cur = n[0][1]
        ans = 0
        for s ,e in n[1:]:
            if s < cur:
                cur = min(cur,e)
                ans +=1
            else:
                cur = e
        return ans
a = solution()
n = [[1,2],[2,3],[1,3]]
print(a.over(n))

       
