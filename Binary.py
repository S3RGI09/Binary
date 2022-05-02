#!/usr/bin/python3

print("\033[1;31m"+"┏┓ ╻┏┓╻┏━┓┏━┓╻ ╻")
print("\033[1;31m"+"┣┻┓┃┃┗┫┣━┫┣┳┛┗┳┛")
print("\033[1;31m"+"┗━┛╹╹ ╹╹ ╹╹┗╸ ╹")

def binario(decimal):
        binario = ""
        while decimal // 2 != 0:
                binario = str(decimal % 2) + binario
                decimal = decimal // 2
        return str(decimal) + binario
print("\033[1;34m"+"-----------------------------------------------------------")
numero = int(input("\033[1;33m"+"Introduce el numero que quieres convertir a binario: "))
print(binario(numero))
print("\033[1;34m"+"-----------------------------------------------------------")
