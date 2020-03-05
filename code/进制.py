# 十进制转二进制，除二倒序取余
from pythonds.basic.stack import Stack


def divide2(desNumber):
    s = Stack()
    while desNumber > 0:
        rem = desNumber % 2
        s.push(rem)
        desNumber = desNumber // 2
    binString = ""
    while not s.isEmpty():
        binString = binString + str(s.pop())
    return binString


print(divide2(233))

# 八进制，十六进制
from pythonds.basic.stack import Stack


def divideBase(desNumber, base):
    digits = '0123456789ABCDEF'
    s = Stack()
    while desNumber > 0:
        rem = desNumber % base
        s.push(rem)
        desNumber = desNumber // base
    binString = ""
    while not s.isEmpty():
        binString = binString + digits[s.pop()]
    return binString


print(divideBase(233, 2))
print(divideBase(233, 8))
print(divideBase(233, 16))


# 十转二

def er():
    print("————十进制转换为二进制————")

    def dec2bin(num):
        l = []
        if num < 0:
            return '-' + dec2bin(abs(num))
        while True:
            num, remainder = divmod(num, 2)
            l.append(str(remainder))
            if num == 0:
                return ''.join(l[::-1])

    a = int(input("请输入一位十进制的数："))
    print("转换为的二进制数为：", dec2bin(a))


while True:
    number = input("请输入一个正数:(输入q退出程序）")
    if number in ['q', 'Q']:
        break
    elif not float(number) > 0:
        print("请输入一个正数（输入q退出程序）：")
    else:
        number = float(number)
        array1 = []
        array2 = []
        integer = int(number)
        floa = number - integer
        while integer != 0:
            array1.append(integer % 2)
            integer = integer // 2
        else:
            array1.append(0)
        array1.reverse()
        while floa > 0.00001:
            array2.append(int(2 * floa))
            floa = floa * 2 - int(floa * 2)
        else:
            array2.append(0)
        array1.append(".")
        array = array1 + array2
        for x in array:
            print(x, end="")
        print("\n")


# 十转八

def ba():
    print("————十进制转换为八进制————")

    def dec2oct(num):
        l = []
        if num < 0:
            return '-' + dec2oct(abs(num))
        while True:
            num, remainder = divmod(num, 8)
            l.append(str(remainder))
            if num == 0:
                return ''.join(l[::-1])

    a = int(input("请输入一位十进制的数："))
    print("转换为的八进制数为：", dec2oct(a))


# 十转十六

def shiliu():
    print("————十进制转换为十六进制————")
    base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]

    def dec2hex(num):
        l = []
        if num < 0:
            return '-' + dec2hex(abs(num))
        while True:
            num, rem = divmod(num, 16)
            l.append(base[rem])
            if num == 0:
                return ''.join(l[::-1])

    a = int(input("请输入一位十进制的数："))
