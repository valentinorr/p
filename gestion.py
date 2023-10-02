class Producto:
    def __init__(self, nombre, precio, categoría):
        self.nombre = nombre
        self.precio = precio
        self.categoría = categoría

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Categoría: {self.categoría}")


class Electrónico(Producto):
    def __init__(self, nombre, precio, categoría, marca, modelo):
        super().__init__(nombre, precio, categoría)
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoría, fecha_de_caducidad):
        super().__init__(nombre, precio, categoría)
        self.fecha_de_caducidad = fecha_de_caducidad

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Fecha de caducidad: {self.fecha_de_caducidad}")


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoría, talla, color):
        super().__init__(nombre, precio, categoría)
        self.talla = talla
        self.color = color

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            producto.mostrar_detalle()



tienda = Tienda("Tienda de productos")

producto1 = Electrónico("Celular", 500, "Electrónica", "Iphone", "11")
producto2 = Alimenticio("Arroz", 20, "Alimentos", "2022-12-31")
producto3 = Vestimenta("Camisa", 30, "Vestimenta", "m", "Negra")

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

tienda.mostrar_productos()