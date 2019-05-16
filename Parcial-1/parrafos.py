class Parrafo():
    def __init__(self):
        self.lineas = []

    def agregar_lineas(self, nombre):
        entry = input("\nIngrese parrafo. Para terminar ingresesolamente '.': \n") 
        while entry != ".": 
            self.lineas.append(entry) 
            entry = input("") 
        self.lineas = '\n'.join(self.lineas) 
        f = open(nombre, 'a')
        f.writelines(self.lineas + "\n\n")
        f.close()

            

            