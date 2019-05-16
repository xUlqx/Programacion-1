from documento import Documento

bucle = True
while bucle:
    opcion = input("Ingrese: \n1: Para crear un nuevo documento. \n2: Para abrir un documento existente.\n3: Para editar un documento. ")
    if opcion == '1':
        d1 = Documento()
        d1.crear_documento()
        d1.agregar_pagina()
        

    elif opcion == '2' :
        d1 = Documento()
        d1.show()
        

    if opcion == '3':
        d1 = Documento()
        d1.editar_documento()
        
    else:
        print("Fin de Programa.")
        bucle = False