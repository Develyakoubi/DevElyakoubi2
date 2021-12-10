def func(num):
    
        if num%2==0:
                 #print(' the number is',num,' even')
                 return 'even'
        if num%2!=0:
                # print('the number is',num,' odd')
                return 'odd'
 
num=input('enter number : ')

res=func(int(num))
print(res)
