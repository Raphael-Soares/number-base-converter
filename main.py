from colorama import Fore, Style

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

def print_ascii_interface():
    ascii_interface = """
    ____     _____     __  
    |  _ \   / ____|   /_ | 
    | |_) | | (___      | | 
    |  _ <   \___ \     | | 
    | |_) |  ____) |    | | 
    |____/  |_____/     |_| 

                                           
    """
    print(Fore.BLUE + ascii_interface + Style.RESET_ALL)

def main():
    print_ascii_interface()

    number = input("Digite um número: ")
    base = int(input("Digite a base atual: "))
    new_base = int(input("Digite a nova base: "))

    decimal = to_decimal(number, base)

    if new_base == 10:
        print(Fore.GREEN + "Número convertido para base decimal:", decimal + Style.RESET_ALL)
    else:
        converted_number = to_base(decimal, new_base)
        print(Fore.GREEN + f"Número convertido para base {new_base}:", converted_number + Style.RESET_ALL)

if __name__ == "__main__":
    main()
