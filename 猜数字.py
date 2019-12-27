import random

i = 3
secret = random.randint(1,10)
temp = input('不访猜一下小甲鱼现在心里想的是哪个数字:')    #返回字符型
guess = int(temp)

while i:
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗?!")
        print("哼，猜中了也没有奖励")
        break
    else:
        if guess < secret:
            print("嘿，小了！小了！")
        else:
            print("哥，大了！大了！")
        if i > 1:
            temp = input("猜错了，请重新输入吧:")
            guess = int(temp)
        i-=1

if i == 0:
    print("正确答案是:",secret)    
print("游戏结束，不玩啦")
