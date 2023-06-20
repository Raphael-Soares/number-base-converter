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
{blue}  ____     _____     __  
 |  _ \   / ____|   /_ | 
 | |_) | | (___      | | 
 |  _ <   \___ \     | | 
 | |_) |  ____) |    | | 
 |____/  |_____/     |_| {reset}

    """.format(blue=Fore.BLUE, reset=Style.RESET_ALL)
    print(ascii_interface)

def main():
    print_ascii_interface()

    number = input("{yellow}Digite um número:{reset} ".format(yellow=Fore.YELLOW, reset=Style.RESET_ALL))
    base = int(input("{yellow}Digite a base atual:{reset} ".format(yellow=Fore.YELLOW, reset=Style.RESET_ALL)))
    new_base = int(input("{yellow}Digite a nova base:{reset} ".format(yellow=Fore.YELLOW, reset=Style.RESET_ALL)))

    decimal = to_decimal(number, base)

    if new_base == 10:
        print("{green}Número convertido para base decimal:{reset} {decimal}".format(green=Fore.GREEN, reset=Style.RESET_ALL, decimal=decimal))
    else:
        converted_number = to_base(decimal, new_base)
        print("{green}Número convertido para base {new_base}:{reset} {converted_number}".format(green=Fore.GREEN, reset=Style.RESET_ALL, new_base=new_base, converted_number=converted_number))

if __name__ == "__main__":
    main()
