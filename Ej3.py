class Producto: # Define la clase Producto
    def __init__(self, nombre, precio, stock): # Define el constructor con los atributos nombre, precio y stock
        self.nombre = nombre # Inicializa el atributo nombre
        self.precio = precio # Inicializa el atributo precio
        self.stock = stock # Inicializa el atributo stock

    def mostrar_informacion(self): # Define el método para mostrar la información del producto
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}") # Imprime la información del producto

    def actualizar_stock(self, cantidad): # Define el método para actualizar el stock del producto
        self.stock += cantidad # Aumenta el stock del producto en base a la cantidad proporcionada

# Crea dos objetos de la clase Producto
producto1 = Producto("Producto 1", 100, 50)
producto2 = Producto("Producto 2", 200, 30)

# Muestra la información de ambos productos
producto1.mostrar_informacion()
producto2.mostrar_informacion()

# Actualiza el stock del primer producto en +10 unidades
producto1.actualizar_stock(10)

# Muestra nuevamente la información del primer producto
producto1.mostrar_informacion()