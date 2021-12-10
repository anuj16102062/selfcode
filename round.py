def round(num):
    for i in range(len(num)):
        a = (num[i] // 10)*10
        b = a+10
        if num[i] - a > b - num[i]:
            num[i] = b
        else:
            num[i] =a
    sum = 0
    for i in range(len(num)):
        sum+=num[i]
    print(sum)
n = [16,19,14]
round(n)
def round(num):
    for i in range(len(num)):
        if num[i] // 10 == 0 and num[i] >= 5:
            num[i] = 10
        elif num[i] // 10 == 0 and num[i] < 5:
            num[i] = 0
        elif num[i] %10 >=5:
            num[i] = num[i] + 10 - num[i] %10
        elif num[i] %10 < 5:
            num[i] = num[i] - num[i]%10 
            
    sum = 0
    for i in range(len(num)):
        sum+=num[i]
    print(sum)
n = [6,9,4,19,14]
round(n)
