class NodoProducto:
    def __init__(self, nombre:str, precio:float=None, stock:int=None, es_producto:bool=False):
        self.nombre = nombre
        self.precio = precio
        self.es_producto = es_producto
        self.stock = stock
        self.hijos:dict = {}

    def agregar_hijo(self, nodo):
        self.hijos[nodo.nombre] = nodo

    def buscar_camino(self, destino, camino=None):       
        if camino is None:
            camino:list = []
        
        camino.append(self.nombre)
        
        if self.nombre == destino:
            return camino
        
        for hijo in self.hijos.values():            
            camino_encontrado = hijo.buscar_camino(destino, camino[:])           
            if camino_encontrado:
                return camino_encontrado
        
        return None
    
    def eliminar_hijo(self, nombre_hijo):        
        if nombre_hijo in self.hijos:
            del self.hijos[nombre_hijo]
        else:
            print(f"No se encontró el hijo con nombre {nombre_hijo} para eliminar.")


class SistemaProductos:
    
    def __init__(self):
        self.raiz = NodoProducto("Catálogo de Productos")

    def agregar_categoria(self, nombre:str, ruta:str=None):
        if not ruta:  # Si ruta es None o cadena vacía
            nuevo_nodo_categoria = NodoProducto(nombre)
            self.raiz.agregar_hijo(nuevo_nodo_categoria)
            return
        nodos = ruta.split("/")
        nodo_actual = self.raiz
        
        for nombre_nodo in nodos:
            if nombre_nodo not in nodo_actual.hijos:
                nuevo_nodo = NodoProducto(nombre_nodo)
                nodo_actual.agregar_hijo(nuevo_nodo)
            nodo_actual = nodo_actual.hijos[nombre_nodo]      
        nuevo_nodo_categoria = NodoProducto(nombre)        
        nodo_actual.agregar_hijo(nuevo_nodo_categoria)  
    def buscar_nodo_categoria(self, nombre: str):        
        def _buscar(nodo, destino):
            if nodo.nombre == destino:
                return nodo
            for hijo in nodo.hijos.values():
                resultado = _buscar(hijo, destino)
                if resultado:
                    return resultado
            return None
        return _buscar(self.raiz, nombre)  
    def agregar_producto(self, categoria:str, nombre:str, precio:float, stock:int):
        nodo_categoria = self.buscar_nodo_categoria(categoria)
        if nodo_categoria:
            nuevo_nodo_producto = NodoProducto(nombre, precio, stock, es_producto=True)
            nodo_categoria.agregar_hijo(nuevo_nodo_producto)
        else:
            print(f"No se encontró la categoría {categoria} para agregar el producto {nombre}.")
        



sistema = SistemaProductos()
print(sistema.raiz.hijos)
sistema.agregar_categoria("Laptops", "Electrónica/Computadoras")
print(sistema.raiz.hijos)
print(sistema.raiz.hijos["Electrónica"].hijos["Computadoras"].hijos)

print(sistema.buscar_nodo_categoria("Laptops"))
sistema.agregar_categoria("Tablets")
print(sistema.raiz.hijos)

print(sistema.buscar_nodo_categoria("Ppas"))

sistema.agregar_producto("Laptops", "Dell XPS 13", 999.99, 10)
print(sistema.raiz.hijos["Electrónica"].hijos["Computadoras"].hijos["Laptops"].hijos)
