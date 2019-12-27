i = 0
def mov(x,n,y):
    global i
    i += 1
    print(i,'. Move disk ',n,'from ',x,' to ',y)

def hanoi(n,x,y,z):
    if n == 1:
        mov(x,1,z)
    else :
        hanoi(n-1,x,z,y)
        mov(x,n,z)
        hanoi(n-1,y,x,z)

a = int(input('请输入hanoi塔的层数:'))
hanoi(a,'x','y','z')
