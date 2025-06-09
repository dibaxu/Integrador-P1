# main.py
# Sistema de Gestión de Productos con Árbol de Categorías

class NodoProducto:
    def __init__(self, nombre: str, precio: float = None, stock: int = None, es_producto: bool = False):
        self.nombre = nombre
        self.precio = precio
        self.es_producto = es_producto
        self.stock = stock
        self.hijos: dict = {}

    def agregar_hijo(self, nodo):
        if nodo.nombre in self.hijos:
            print(f"Error: Ya existe un hijo con el nombre '{nodo.nombre}'.")
            return
        self.hijos[nodo.nombre] = nodo
        
    def listar_productos(self):
        productos = []
        if self.es_producto:
            productos.append(self)
        for hijo in self.hijos.values():
            productos.extend(hijo.listar_productos())
        return productos

    def actualizar_producto(self, nuevo_nombre=None, nuevo_precio=None, nuevo_stock=None):
        if not self.es_producto:
            print("Error: No se puede actualizar una categoría.")
            return
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_precio is not None:
            self.precio = nuevo_precio
        if nuevo_stock is not None:
            self.stock = nuevo_stock
        print(f"Producto '{self.nombre}' actualizado.")


class SistemaProductos:
    def __init__(self):
        self.raiz = NodoProducto("Catálogo de Productos")

    # ----- Búsqueda -----
    def buscar_nodo(self, nombre: str, nodo_inicial=None):
        # Función de búsqueda genérica (para productos o categorías)
        if nodo_inicial is None:
            nodo_inicial = self.raiz

        def _buscar(nodo, destino):
            if nodo.nombre == destino:
                return nodo
            for hijo in nodo.hijos.values():
                resultado = _buscar(hijo, destino)
                if resultado:
                    return resultado
            return None
        return _buscar(nodo_inicial, nombre)

    # ----- Categorías -----
    def agregar_categoria(self, nombre: str, ruta_padre: str = None):
        # CORREGIDO: La lógica ahora es más clara. Se busca la categoría padre por su nombre.
        nodo_padre = self.raiz
        if ruta_padre:
            nodo_padre = self.buscar_nodo(ruta_padre)
            if not nodo_padre or nodo_padre.es_producto:
                print(f"Error: La categoría padre '{ruta_padre}' no existe o es un producto.")
                return

        if nombre in nodo_padre.hijos:
            print(f"Error: La categoría '{nombre}' ya existe en '{nodo_padre.nombre}'.")
            return
            
        nueva_categoria = NodoProducto(nombre)
        nodo_padre.agregar_hijo(nueva_categoria)
        print(f"✅ Categoría '{nombre}' agregada en '{nodo_padre.nombre}'.")

    def eliminar_categoria(self, nombre_categoria: str):
        # CORREGIDO: Se implementó la llamada a la función interna y se manejan los resultados.
        def _encontrar_y_eliminar_padre(nodo_actual):
            if nombre_categoria in nodo_actual.hijos:
                nodo_a_eliminar = nodo_actual.hijos[nombre_categoria]
                if nodo_a_eliminar.es_producto:
                    return "es_producto" # No es una categoría
                if nodo_a_eliminar.hijos:
                    return "no_vacia" # No se puede eliminar si tiene hijos
                
                del nodo_actual.hijos[nombre_categoria]
                return "exito"

            for hijo in nodo_actual.hijos.values():
                if not hijo.es_producto:
                    resultado = _encontrar_y_eliminar_padre(hijo)
                    if resultado:
                        return resultado
            return None

        resultado = _encontrar_y_eliminar_padre(self.raiz)
        if resultado == "exito":
            print(f"🗑️ Categoría '{nombre_categoria}' eliminada correctamente.")
        elif resultado == "no_vacia":
            print(f"Error: No se puede eliminar la categoría '{nombre_categoria}' porque no está vacía.")
        elif resultado == "es_producto":
            print(f"Error: '{nombre_categoria}' es un producto, no una categoría.")
        else:
            print(f"Error: No se encontró la categoría '{nombre_categoria}'.")
            
    # ----- Productos -----
    def agregar_producto(self, categoria: str, nombre: str, precio: float, stock: int):
        nodo_categoria = self.buscar_nodo(categoria)
        if nodo_categoria and not nodo_categoria.es_producto:
            if nombre in nodo_categoria.hijos:
                print(f"Error: Ya existe un item con el nombre '{nombre}' en '{categoria}'.")
                return
            nuevo_producto = NodoProducto(nombre, precio, stock, es_producto=True)
            nodo_categoria.agregar_hijo(nuevo_producto)
            print(f"✅ Producto '{nombre}' agregado a la categoría '{categoria}'.")
        else:
            print(f"Error: No se encontró la categoría '{categoria}'.")
            
    def eliminar_producto(self, nombre_producto: str):
        # NUEVA FUNCIÓN: Permite eliminar un producto buscándolo en todo el árbol.
        def _encontrar_y_eliminar_padre(nodo_actual):
            if nombre_producto in nodo_actual.hijos:
                nodo_a_eliminar = nodo_actual.hijos[nombre_producto]
                if not nodo_a_eliminar.es_producto:
                    return False # No es un producto
                
                del nodo_actual.hijos[nombre_producto]
                return True

            for hijo in nodo_actual.hijos.values():
                if not hijo.es_producto: # Solo buscar dentro de categorías
                    if _encontrar_y_eliminar_padre(hijo):
                        return True
            return False
            
        if _encontrar_y_eliminar_padre(self.raiz):
            print(f"🗑️ Producto '{nombre_producto}' eliminado correctamente.")
        else:
            print(f"Error: No se encontró el producto '{nombre_producto}' o es una categoría.")

    # ----- Visualización -----
    def mostrar_arbol(self, nodo=None, prefijo=""):
        # Función útil para visualizar la estructura del árbol.
        if nodo is None:
            nodo = self.raiz
        
        # Determina si es el último hijo para dibujar las líneas correctamente
        hijos = list(nodo.hijos.values())
        for i, hijo in enumerate(hijos):
            conector = "└── " if i == len(hijos) - 1 else "├── "
            if hijo.es_producto:
                print(f"{prefijo}{conector}📦 {hijo.nombre} (Precio: ${hijo.precio}, Stock: {hijo.stock})")
            else:
                print(f"{prefijo}{conector}📁 {hijo.nombre}")
                # Prepara el prefijo para la siguiente llamada recursiva
                nuevo_prefijo = prefijo + ("    " if i == len(hijos) - 1 else "│   ")
                self.mostrar_arbol(hijo, nuevo_prefijo)

# ------------------------------------------------------------------------------------
# -------- PASO A PASO PARA PROBAR EL CÓDIGO --------
# ------------------------------------------------------------------------------------

if __name__ == "__main__":
    # 1. Creamos una instancia de nuestro sistema
    sistema = SistemaProductos()
    print("🚀 Sistema de Gestión de Productos iniciado.")
    print("==========================================")

    # 2. Agregamos categorías principales
    print("\nPASO 1: Agregando categorías principales...")
    sistema.agregar_categoria("Almacén")
    sistema.agregar_categoria("Lácteos")
    sistema.agregar_categoria("Limpieza")
    
    # 3. Agregamos una subcategoría dentro de "Almacén"
    print("\nPASO 2: Agregando subcategorías...")
    sistema.agregar_categoria("Bebidas", ruta_padre="Almacén")
    sistema.agregar_categoria("Galletitas", ruta_padre="Almacén")
    # Intentamos agregar en una categoría que no existe (mostrará un error)
    sistema.agregar_categoria("Jugos", ruta_padre="Bebidas sin gas") 
    
    print("\nÁrbol de categorías actual:")
    sistema.mostrar_arbol()
    print("==========================================")

    # 4. Agregamos productos a las categorías
    print("\nPASO 3: Agregando productos...")
    sistema.agregar_producto("Lácteos", "Leche Entera", 150.50, 50)
    sistema.agregar_producto("Lácteos", "Yogur de Frutilla", 99.99, 30)
    sistema.agregar_producto("Bebidas", "Gaseosa Cola", 250.0, 100)
    sistema.agregar_producto("Limpieza", "Lavandina", 120.0, 40)
    
    print("\nÁrbol con productos:")
    sistema.mostrar_arbol()
    print("==========================================")

    # 5. Listamos todos los productos de una categoría específica
    print("\nPASO 4: Listando productos de 'Lácteos'...")
    nodo_lacteos = sistema.buscar_nodo("Lácteos")
    if nodo_lacteos:
        productos_lacteos = nodo_lacteos.listar_productos()
        for p in productos_lacteos:
            print(f" - {p.nombre}: ${p.precio}")
    print("==========================================")

    # 6. Actualizamos un producto
    print("\nPASO 5: Actualizando el precio y stock de 'Leche Entera'...")
    producto_leche = sistema.buscar_nodo("Leche Entera")
    if producto_leche:
        producto_leche.actualizar_producto(nuevo_precio=165.0, nuevo_stock=45)
    
    print("\nÁrbol después de la actualización:")
    sistema.mostrar_arbol()
    print("==========================================")
    
    # 7. Eliminamos un producto y una categoría
    print("\nPASO 6: Eliminando el producto 'Yogur de Frutilla' y la categoría 'Galletitas'...")
    sistema.eliminar_producto("Yogur de Frutilla")
    # Intentamos eliminar una categoría con productos (mostrará error)
    sistema.eliminar_categoria("Lácteos") 
    # Eliminamos una categoría vacía
    sistema.eliminar_categoria("Galletitas")

    print("\nÁrbol final:")
    sistema.mostrar_arbol()
    print("==========================================")
    print("✅ Prueba finalizada.")