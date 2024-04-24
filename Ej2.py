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

# Crear dos objetos de tipo Empleado
empleado1 = Empleado("Juan", "Perez", 30, 50000)
empleado2 = Empleado("Ana", "Gomez", 28, 55000)

# Mostrar la información de ambos empleados
empleado1.mostrar_informacion()
empleado2.mostrar_informacion()

# Aumentar el salario del primer empleado en un 10%
empleado1.aumentar_salario(10)

# Mostrar nuevamente la información del primer empleado
empleado1.mostrar_informacion()