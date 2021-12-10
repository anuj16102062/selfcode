def funp(n):
	if n%10 == n:
		return n
	else:
		return (n%10) * funp(n//10)
ans = funp(144)
print(ans)
def funp(n):
	product = 1
	if n == 0:
		return 0
	else:
		return (n%10) + funp(n//10)
ans = funp(144)
print(ans)

def findzeros(n,c):
	if n ==0:
		return print(c)
	rem = n %10
	if rem == 0:
		return findzeros(n//10,c+1)
	else:
		return findzeros(n//10,c)
findzeros(1050,0)
def reverse(n):
	sum = 0
	while n > 0:
		rem = n %10
		sum = sum * 10 + rem
		n = n //10
	print(sum)
reverse(144)