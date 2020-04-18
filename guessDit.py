#coding=GBK
import random

'''
猜字游戏
随机生成一个 0,100间的整数
'''
def guessDit():
    target=random.randint(0,100)
    cnt = 0
    while True:
        pre=input("请输入你的答案:")
        cnt+=1
        if (pre == target):
            print "恭喜你答对了"
            break
        elif (pre > target):
            print "大了"
        else:
            print "小了"

    print "正确数为：%d,你一共用了 %d 次" %(target,cnt)

if __name__ == "__main__":
    guessDit()

