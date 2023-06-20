def to_decimal(number, base):
    decimal = 0
    for num in number:
        decimal = decimal * base + int(num)
    return decimal

def to_base(decimal, base):
    digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        result = digits[decimal % base] + result
        decimal = decimal // base
    return result

def main():
    number = input("Digite um número: ")
    base = int(input("Digite a base atual: "))
    new_base = int(input("Digite a nova base: "))

    decimal = to_decimal(number, base)

    if new_base == 10:
        print("Número convertido para base decimal:", decimal)
    else:
        converted_number = to_base(decimal, new_base)
        print("Número convertido para base", new_base, ":", converted_number)

if __name__ == "__main__":
    main()
