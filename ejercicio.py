class Paciente:
    #ATRIBUTOS
    def __init__(self):
        self.nombre = ""
        self.cedula = 0
        self.genero = ""
        self.servicio = ""
    
    print('Hola como estas')
    
    
    
    print()
    
    

    #METODOS
    def verCedula(self):
        return self.cedula
    
    def verServicio(self):
        return self.servicio
    
    def verGenero(self):
        return self.genero
    
    def verNombre(self):
        return self.nombre
    
    
    def asignarNombre(self,n):
        self.nombre = n
    def asignarServicio(self,s):
        self.servicio = s
    def asignarGenero(self,g):
        self.genero = g
    def asignarCedula(self,c):
        self.cedula = c

class Sistema:
    def __init__(self):
        self.lista_pacientes = []
        self.numero_pacientes = len(self.lista_pacientes)
        
        #METODOS
    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        cedula = int(input("Ingrese la cédula del paciente: "))
        genero = input("Ingrese el género del paciente: ")
        servicio = input("Ingrese el servicio: ")
        
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self.lista_pacientes.append(p)
        self.numero_pacientes = len(self.lista_pacientes)
    
    def verNumeroPacientes(self):
        return self.numero_pacientes
    
    def verDatosPaciente(self):
        cedula=int(input("Ingrese cédula a buscar: "))
        for paciente in self.lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: "+ paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

mi_sistema = Sistema()

while True:
    opcion = int(input("1. nuevo paciente - 2. Numero de pacientes - 3. Datos pacientes - 4. Salir"))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opción Invalida")