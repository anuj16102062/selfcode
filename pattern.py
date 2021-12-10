def pypart2(n):
    for i in range(0,10):
        if   i >= 5:
            col = n - i - 1
            for j in range(col):
                print("* ", end="")
        else :
            for j in range(0, i+1):
         
            # printing stars
                print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 10
pypart2(n)

