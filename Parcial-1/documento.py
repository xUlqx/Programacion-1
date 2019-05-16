from paginas import Pagina
import os

class Documento():
    def __init__(self):
        self.paginas = []
        self.nombre = ""

    def crear_documento(self):
        archivo = input("Ingrese el nombre del Documento: ")
        self.nombre = archivo
        f = open(self.nombre, 'w')
        f.close() 
        print(f"El archivo {archivo} fue creado exitosamente.\n")
    
    def agregar_pagina(self):
        
        bucle = True
        self.paginas = Pagina()
        self.paginas.agregar_encabezado(self.nombre)
        while bucle:
            self.paginas.agregar_parrafo(self.nombre)
            respuesta = input("¿Desea agregar otro parrafo? (s=SI n=NO) ")
            if(respuesta.capitalize() == 'N'):
                bucle = False
            
        self.paginas.agregar_pie(self.nombre)

    def editar_documento(self):

        nombre = input("Ingrese nombre o ruta del archivo a abrir: ")
        bucle = True
        self.paginas = Pagina()
        self.paginas.agregar_encabezado(nombre)
        while bucle:
            self.paginas.agregar_parrafo(nombre)
            respuesta = input("¿Desea agregar otro parrafo? (s=SI n=NO) ")
            if(respuesta.capitalize() == 'N'):
                bucle = False
            
        self.paginas.agregar_pie(nombre)
            


    def show(self):
        try: 
            nombre = input("Ingrese nombre o ruta del archivo a abrir: ")
            f = open(nombre, 'r') 
            text = f.read() 
            #f = os.popen(self.nombre, 'r') 
            print(f"\n------------------Archivo {nombre}--------------------\n")
            print(text)
           
            f.close()
  
        except IOError:     
            print('Error en la lectura del archivo : ' + self.nombre)