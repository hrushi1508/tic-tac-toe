l=[2,2,3,4,5,6,7,8,9]
s=[];b=0
count=0
for k in range(0,9):  
    if k%2==0:
        print("player 1 turn")
    else:
        print("player 2 turn")
    b=int(input('enter the positon btw 1 to 9\n'))
    if k%2==0:
        l[b-1]=1
    else:
        l[b-1]=0
    s.append(b)
    count+=1
    for i in range(0,9):
        if l[i]==1 or l[i]==0:
            if l[i]==1:
                print('x','|',end='')
            elif l[i]==0:
                print('0','|',end='')
            else:
                print('enter a number btw 1 to 9')
        else:
            print(' ',"|",end='')
        if i==2:
            print('')
            print("---------")
        elif i==5:
            print('')
            print("---------")
    print('')
    if l[0]==l[1]==l[2]:
        break
    elif l[0]==l[3]==l[6]:
        break
    elif l[0]==l[4]==l[8]:
        break
    elif l[1]==l[3]==l[7]:
        break
    elif l[2]==l[5]==l[8]:
        break
    elif l[6]==l[4]==l[2]:
        break
    elif l[6]==l[7]==l[8]:
        break
    elif l[3]==l[4]==l[5]:
        break
    elif count==9:
        break
print('')
if count==9:
    print("Draw")
elif k%2==0:
    print("player 1 is the winner")
else:
    print("player 2 is the winner")
