def fun(n,step):
	if n ==0:
		return print(step)
	elif n % 2 ==0:
		return fun(n//2,step+1)
	else:
		fun(n-1,step+1)
fun(14,0)