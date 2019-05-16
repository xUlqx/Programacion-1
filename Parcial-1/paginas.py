from parrafos import Parrafo

class Pagina():
    def __init__(self):
        self.encabezado = ""
        self.parrafos = []
        self.pie = ""

    def agregar_encabezado(self, nombre):
        self.encabezado = input("Ingrese Encbezado: ")
        f = open(nombre, 'w')
        f.write("\n" + self.encabezado + "\n\n")
        f.close()
      

        

    def agregar_parrafo(self, nombre):
        self.parrafos = Parrafo()
        self.parrafos.agregar_lineas(nombre)
           

    def agregar_pie(self, nombre):
        self.pie = input("Ingrese Pie: ")
        try: 
            f = open(nombre, 'a')
            f.write(self.pie)
            f.close()

        except IOError:     
            print('Error en la lectura del archivo : ' + nombre)