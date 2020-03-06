# 递归
# 由于python没有做递归优化，所以超过1000次递归调用就会爆栈


import sys


# 尾递归函数fib被tail_call_optimized装饰, 则fib这个名字实际所指的function object变成了tail_call_optimized里return的_wrapper, fib 指向_wrapper
# 注意_wrapper里return func(*args, **kwargs)这句, 这个func还是未被tail_call_optimized装饰的fib（装饰器的基本原理）, func是实际的fib, 我们称之为real_fib
# 当执行fib(1200, 0, 1)时, 实际是执行_wrapper的逻辑, 获取帧对象也是_wrapper对应的, 我们称之为frame_wapper
# 由于我们是第一次调用, 所以”if f.f_back and f.f_back.f_back and f.f_code == f.f_back.f_back.f_code”这句里f.f_code==f.f_back.f_back.f_code显然不满足
# 继续走循环, 内部调用func(*args, **kwargs), 之前说过这个func是没被装饰器装饰的fib, 也就是real_fib
# 由于是函数调用, 所以虚拟机会创建real_fib的栈帧, 我们称之为frame_real_fib, 然后执行real_fib里的代码, 此时当前线程内的栈帧链表按从旧到新依次为: 旧的虚拟机栈帧，frame_wrapper，frame_real_fib(当前执行帧)

class TailCallException(BaseException):
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tail_call_optimized(func):
    def _wrapper(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_code == f.f_back.f_back.f_code:
            raise TailCallException(args, kwargs)

        else:
            while True:
                try:
                    return func(*args, **kwargs)
                except TailCallException as why:
                    args = why.args
                    kwargs = why.kwargs

    return _wrapper


@tail_call_optimized
def sum1(n, total=0):
    if n == 0:
        return total
    return sum1(n - 1, total + n)


print(sum1(1000))


# 来自力扣练习题，不用任何数学方法或者直接交互，实现简单计算
# 感觉可以使用递归来做，但是还没有实现
# (1+(5+3+6)-4)-(5+6)
# -20-11
def cover(s):
    s = s.replace(' ', '')

    def sum(s_str):
        s_str = s_str.replace('--', '+').replace('-+', '-').replace('+-', '-')
        s = []
        i = 0
        while i < len(s_str):
            if not s_str[i].isdigit():
                s.append(s_str[i])
                i += 1
            else:
                m = 0
                for n in range(len(s_str[i:])):
                    if s_str[i + n].isdigit():
                        m += 1
                    else:
                        break
                s.append(s_str[i:i + m])
                i += m

        if s[0].isdigit():
            s_sum = int(s[0])
        else:
            s_sum = 0
            s.insert(0, s_sum)

        for i in range(1, len(s)):
            if not s[i].isdigit():
                if s[i] == '+':
                    s_sum += int(s[i + 1])
                else:
                    s_sum -= int(s[i + 1])
        print(s_sum, eval(s_str))
        print(s)
        return s_sum

    while 1:
        if '(' in s:
            end = s.find(')')
            start = s[:end].rfind('(')
            sum_s = sum(s[start + 1:end])
            s = s.replace(s[start:end + 1], str(sum_s), 1)
        else:
            break

    s_sum = sum(s)
    print(s_sum)
    return s_sum


# cover(' 1+1-1 +1+2- 5+7+8 -1+5- 4+5-7+5- 6+2-4+5- 7+8-4')
# cover('(1+( 5+3+6)- 4) -(5+6)')
# cover("1-(2+3-(4+(5-(1-(2+4-(5+6))))))")


# [1,3,5,7,9]

def listSum(numList):
    sum = 0
    for i in numList:
        sum = sum + i

    return sum


print(listSum([1, 3, 5, 7, 9]))

'''
    listSum2([1,3,5,7,9]) 
  = 1 + listSum2([3,5,7,9])
  = 3 + listSum2([5,7,9])
  = 5 + listSum2([7,9])
  = 7 + listSum2([9])
'''


def listSum2(numList):  # 递归函数：调用自身的函数
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum2(numList[1:])


print(listSum2([1, 3, 5, 7, 9]))


def toStr(n, base):
    str1 = '0123456789ABCDEF'
    # 比如0，1 < 2
    if n < base:
        return str1[n]
    else:
        return toStr(n // base, base) + str1[n % base]


print(toStr(5686, 16))

# 可视化递归算法
# 递归绘制螺旋
# import turtle

# myTurtle = turtle.Turtle()  #  画笔对象
# myScreen = turtle.Screen()  #  窗口

# def drawSpiral(myTurtle,lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen - 5)

# drawSpiral(myTurtle,100)
# myScreen.exitonclick()


# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(45)
#         tree(branchLen-15,t)
#         t.left(90)
#         tree(branchLen-15,t)
#         t.right(45)
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myScreen = turtle.Screen()

#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("red")
#     tree(75,t)
#     myScreen.exitonclick()

# main()


from pythonds.basic.stack import Stack


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height - 1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height - 1, withPole, toPole, fromPole)


def moveDisk(fp, tp):
    print("移动盘子，从", fp, "到", tp)


fromPole = Stack()
toPole = Stack()
withPole = Stack()

moveTower(5, fromPole, toPole, withPole)
