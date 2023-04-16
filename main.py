number = input("Digite um número: ")
base = int(input("Digite a base: "))

newBase = int(input("Digite a nova base: "))


def toDecimal(number, base):
    decimal = 0
    for num in number:
        decimal = decimal * base + int(num)

    if newBase == 10:
        print(decimal)
        return
    elif newBase == 16:
        toHexa(decimal)
        return

    toBase(decimal, newBase)


def toBase(decimal, base):
    result = ""
    while decimal > 0:
        result = str(decimal % base) + result
        decimal = decimal // base

    print(result)


def toHexa(decimal):
    hexa = ""
    while decimal > 0:
        hexa = str(decimal % 16) + hexa
        decimal = decimal // 16

    print(hexa)


toDecimal(number, base)
