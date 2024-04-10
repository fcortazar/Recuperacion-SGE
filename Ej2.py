class Empleado: # Creamos la clase empleado
    def __init__(self, nombre, apellido, edad, salario): # Definimos el constructor de la clase
        self.nombre = nombre # Inicializamos el atributo nombre
        self.apellido = apellido # Inicializamos el atributo apellido
        self.edad = edad # Inicializamos el atributo edad
        self.salario = salario # Inicializamos el atributo salario

    def mostrar_informacion(self): # Definimos el método mostrar_informacion
        print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nSalario: {self.salario}") # Imprimimos la información del empleado

    def aumentar_salario(self, porcentaje): # Definimos el método aumentar_salario
        self.salario += self.salario * (porcentaje / 100) # Aumentamos el salario del empleado