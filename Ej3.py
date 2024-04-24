class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}")

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

# Crear dos objetos de tipo Producto
producto1 = Producto("Producto 1", 100, 50)
producto2 = Producto("Producto 2", 200, 30)

# Mostrar la información de ambos productos
producto1.mostrar_informacion()
producto2.mostrar_informacion()

# Actualizar el stock del primer producto en +10 unidades
producto1.actualizar_stock(10)

# Mostrar nuevamente la información del primer producto
producto1.mostrar_informacion()