## Integrantes

- Franco Siri
- Pedro Antonio Sota Taier

- **Video**: https://youtu.be/KO8ORZHhQRY

**Programación 1 - Tecnicatura en Programación - UTN**

- **Profesor**: Prof. Nicolás Quirós
- **Tutor**: Matias Santiago Torres
- **Comisión 22**

## Clase NodoProducto

La clase `NodoProducto` representa un nodo dentro de una estructura de tipo árbol para organizar productos y categorías.

### Atributos

- **nombre** (`str`): Nombre del producto o categoría.
- **precio** (`float`, opcional): Precio del producto. Puede ser `None` si es una categoría.
- **stock** (`int`, opcional): Cantidad en stock del producto. Puede ser `None` si es una categoría.
- **es_producto** (`bool`): Indica si el nodo es un producto (`True`) o una categoría (`False`).
- **hijos** (`dict`): Diccionario de nodos hijos, donde la key es el nombre y el value es el nodo hijo.

### Métodos

- **agregar_hijo(nodo)**: Agrega un nodo hijo al nodo actual. Si ya existe un hijo con ese nombre, muestra un error.
- **listar_productos()**: Devuelve una lista de todos los productos (nodos con `es_producto=True`) que se ramifican de este nodo, incluyendo subcategorías.
- **actualizar_producto(nuevo_nombre, nuevo_precio, nuevo_stock)**: Permite modificar el nombre, precio o stock de un producto. No se puede usar en categorías.

Esta clase permite construir y manipular árboles de productos y categorías de manera flexible.

## Clase SistemaProductos

La clase `SistemaProductos` administra un árbol de productos y categorías utilizando nodos de la clase `NodoProducto`. Sirve para organizar productos en categorías jerárquicas, agregar nuevas categorías y productos, y buscar categorías dentro del árbol.

### Métodos

- **__init__()**
  - Inicializa el sistema con un nodo raíz llamado "Catálogo de Productos".

- **buscar_nodo(nombre: str, nodo_inicial=None)**
  - Busca y retorna el nodo cuyo nombre coincide con el argumento, recorriendo el árbol en preorden.
  - Si no se encuentra, retorna `None`.

- **agregar_categoria(nombre: str, ruta_padre: str = None)**
  - Agrega una nueva categoría al sistema.
  - Si `ruta_padre` es `None` o una cadena vacía, la categoría se agrega como hija directa de la raíz.
  - Si se especifica una ruta, la categoría se agrega como hija de la categoría indicada por `ruta_padre`.
  - Si la categoría ya existe en ese nivel, muestra un error.

- **eliminar_categoria(nombre_categoria: str)**
  - Elimina una categoría si está vacía (no tiene hijos).
  - Si la categoría tiene productos o subcategorías, muestra un error.
  - Si el nombre corresponde a un producto, muestra un error.

- **agregar_producto(categoria: str, nombre: str, precio: float, stock: int)**
  - Agrega un producto como hijo de la categoría indicada.
  - Si la categoría no existe o el nombre ya existe en esa categoría, muestra un error.

- **eliminar_producto(nombre_producto: str)**
  - Elimina un producto buscándolo en todo el árbol.
  - Si el nombre corresponde a una categoría o no se encuentra, muestra un error.

- **mostrar_arbol(nodo=None, prefijo="")**
  - Muestra la estructura del árbol de categorías y productos de forma visual y jerárquica.

---

### Funcionamiento

- El sistema permite construir una jerarquía de categorías y productos.
- Las categorías pueden anidarse unas dentro de otras.
- Los productos solo pueden agregarse como hijos de una categoría existente.
- La búsqueda de categorías y productos se realiza por nombre, recorriendo todo el árbol en preorden.
- Se pueden eliminar productos y categorías (solo si están vacías).
- Se puede actualizar la información de los productos.
- Se puede visualizar el árbol completo de manera jerárquica.

---

## Lista de mejoras o revisiones

1. Interfaz gráfica de usuario para facilitar la interacción
2. Análisis de datos y generación de reportes automatizados
3. Validación de rutas.
4. Métodos para guardar y cargar la estructura en archivos (por ejemplo, JSON).
5. Métodos para agregar/disminuir stock.

---

**Ejemplo de uso:**  
Ver el bloque `if __name__ == "__main__":` en el archivo principal para un paso a paso de cómo utilizar el sistema.

