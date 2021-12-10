def prime(l,u):
    for i in range(l,u+1):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    print(i,'non prime')
                    break
            else :
                print('prime',i)
prime(1,15)

        
        
            
            
