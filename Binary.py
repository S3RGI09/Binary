print("┏┓ ╻┏┓╻┏━┓┏━┓╻ ╻")
print("┣┻┓┃┃┗┫┣━┫┣┳┛┗┳┛")
print("┗━┛╹╹ ╹╹ ╹╹┗╸ ╹")
print("Creado por S3RGI09 (Sergio Casero Verdial)")
def binario(decimal):
        binario = ""
        while decimal // 2 != 0:
                binario = str(decimal % 2) + binario
                decimal = decimal // 2
        return str(decimal) + binario
print("-----------------------------------------------------------")
numero = int(input("Introduce el numero que quieres convertir a binario: "))
print(binario(numero))
print("-----------------------------------------------------------")
