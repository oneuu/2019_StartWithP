print('判断阿姆斯特朗数字，请输入一个数字: (退出请输入exit)')

while True:
    intext = str(input(">>>"))
    if intext == "exit":
        print('Bye~')
        exit(0)
    else:
        try:
            num = int(intext)
        except ValueError:
            print ('请输入阿拉伯数字！')
            continue
        sum = 0
        n = len(str(num))
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if num == sum:
            print(num, '是阿姆斯特朗数')
        else:
            print(num, "不是阿姆斯特朗数")
            前卫2
            qweqwe
