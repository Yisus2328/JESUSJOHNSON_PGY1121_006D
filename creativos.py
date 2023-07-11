import funciones as f

while True:
    
    f.limpiarp()
    f.menu()
    opcion=int(input("Seleccione :"))

    if opcion==5:
        f.salir()
        break
    elif opcion==1:
        ent=int(input("Indique la cantidad de entradas (1-3) :"))
        if ent>=1 and ent<=3:
            for i in range(ent):
                f.mostrar()
                fila=int(input("Ingrese la fila que desea comprar :"))
                columna=input("Ingrese la columna :").upper()
                f.comprar(fila,columna)
        else:
            f.printrr("Numero invalido de entradas")
    elif opcion==2:
        f.mostrar()
    elif opcion==3:
        f.asis()
    elif opcion==4:
        f.ganancia()
    else:
        f.printrr("OPCION NO VALIDA")