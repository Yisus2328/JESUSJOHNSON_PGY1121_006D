import msvcrt
import os
import numpy
from colorama import Style, Fore

pl=120000
go=80000
si=50000
p=0
g=0
s=0
entradas=numpy.empty([1,10,10],object)

def printvv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printv(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")

def printrr(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printr(texto):
    print(f"{Fore.RED}{texto}{Fore.RESET}")

def printa(texto):
    print(f"{Fore.YELLOW}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")


def limpiarp():
    printa("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

def menu():
    printvv("""
    #######################
    #### CREATIVOS.CL #####
    #######################""")
    printv("""
    1) Comprar entradas
    2) Mostrar ubicaciones disponibles
    3) Ver listado de asistentes 
    4) Mostrar ganancias totales
    5) Salir""")


columna=["A","B","C","D","E","F","G","H","I","J"]
fila=[10,9,8,7,6,5,4,3,2,1]
def mostrar():
    printvv("""
     ____________________________
    |                            |
    |        ESCENARIO           |
    |____________________________|
    """)
    printa(" A   B   C   D   E   F   G   H   I   J")
    for x in range(10):
        for y in range(10):
            if entradas[0,x,y]==None:
                print(f"🟩 ",end=" ")
            else:
                print("❌",end="  ")   
        
        print(f" {10-x} ")

def comprar(fil,col):
    printvv("Sistema de compras Creativos")
    global p
    global g
    global s
    if fil>=1 and fil<=10:
        if col in columna:
            fi=fila.index(fil)
            co=columna.index(col)
            if entradas[0,fi,co]==None:
                rut=int(input("Ingrese su rut sin guion ni punto ej: 21846752 :"))
                if not rut in entradas:
                    if rut>8:
                        entradas[0,fi,co]=rut
                        printvv("Datos guardados")
                    else:
                        printrr("Rut invalido")

                    if fi==0 or fi==1:
                        printv("ENTRADA PLATINUM COMPRADA ✅ ")
                        p+=1
                    elif fi==2 or fi==3 or fi==4:
                        printv("ENTRADA GOLD COMPRADA ✅ ")
                        g+=1
                    else:
                        printv("ENTRADA SILVER COMPRADA ✅ ")
                        s+=1
                else:
                    printrr("El rut no puede repetirse")
            else:
                printrr("Asiento ya comprado")
        else:
            printrr("COLUMNA NO VALIDA")
    else:
        printrr("NUMERO DE FILA INVALIDO")


def ganancia():
    plt=pl*p
    got=go*g
    sit=si*s
    tt=plt+got+sit
    printvv(f"""
    Tipo entrada    Cantidad    Total
    Platinum ${pl}    {p}       {plt}
    Gold ${go}         {g}       {got}
    Silver ${si}       {s}       {sit}
    -------------------------
    Total               {p+g+s}       {tt}""")

def asis():
    print("Listado de asistentes :")
    for x in range(10):
        for y in range(10):
            if entradas[0,x,y]!=None:
                print(entradas[0,x,y])

def salir():
    printa("""
    Nombre: Jesus Johnson
    Fecha: 11-07-2023""")