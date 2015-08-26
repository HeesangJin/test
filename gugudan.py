__author__ = 'jinheesang'

max = 9
k=2

while k<=max:

    for j in range(2,10,1):
        for i in range(k,k+3,1):
            if i==10:
                break
            print(i,'*',j,'=',i*j,end='  ')
        print('')
    k+=3
    print('')
