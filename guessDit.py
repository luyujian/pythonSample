#coding=GBK
import random

'''
������Ϸ
�������һ�� 0,100�������
'''
def guessDit():
    target=random.randint(0,100)
    cnt = 0
    while True:
        pre=input("��������Ĵ�:")
        cnt+=1
        if (pre == target):
            print "��ϲ������"
            break
        elif (pre > target):
            print "����"
        else:
            print "С��"

    print "��ȷ��Ϊ��%d,��һ������ %d ��" %(target,cnt)

if __name__ == "__main__":
    guessDit()

