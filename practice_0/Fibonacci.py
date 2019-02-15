print("显示斐波那契额数列，请输入数列数量")
num = int(input(">>>"))

n1 = 1
n2 = 1

total = 2
if num < 0:
    print("请输入正整数！")
elif num == n1:
    print("斐波那契数列：", n1)
elif num == n2:
    print("斐波那契数列：", n1, n2, sep=',')
else:
    print("斐波那契数列：", n1, n2, sep=',', end='')
    while total < num:
        sum = n1 + n2
        n1, n2 = n2, sum
        total += 1
        print(",", sum, end='')
print('。')
