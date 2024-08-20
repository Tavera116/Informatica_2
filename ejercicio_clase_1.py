class Persona:
    def __init__(self, nombre, sexo, cc):
        self.nombre = nombre
        self.sexo = sexo                #-----> ATRIBUTOS 
        self.cc = cc                           
          
    def __str__(self):
        return f'{self.nombre}--{self.sexo}---{self.cc}' #-----> METODOS
    
    def Saludar(self):
        return 'Mi nombre es ' + self.nombre
        
        
        
fn = Persona('Juan', 'M', 1040572295)    
        
fn.nombre = 'Juan Manuel'

print(fn.nombre)
print(fn.sexo) 
print(fn.cc) 
print(fn)
print(f'\n{fn.Saludar()}')
 
        