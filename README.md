## Clase NodoProducto

La clase `NodoProducto` representa un nodo dentro de una estructura de tipo árbol para organizar productos y categorías.

### Atributos

- **nombre** (`str`): Nombre del producto o categoría.
- **precio** (`float`, opcional): Precio del producto. Puede ser `None` si es una categoría.
- **stock** (`int`, opcional): Cantidad en stock del producto. Puede ser `None` si es una categoría.
- **es_producto** (`bool`): Indica si el nodo es un producto (`True`) o una categoría (`False`).
- **hijos** (`dict`): Diccionario de nodos hijos, donde la key es el nombre y el value es el nodo hijo.

### Métodos

- **agregar_hijo(nodo)**: Agrega un nodo hijo al nodo actual.
- **buscar_camino(destino, camino=None)**: Busca un camino desde el nodo actual hasta un nodo con nombre igual a `destino`. Devuelve una lista con los nombres del camino encontrado o `None` si no existe.
- **eliminar_hijo(nombre_hijo)**: Elimina un hijo del nodo actual por su nombre.

Esta clase nos permite construir y manipular árboles de productos y categorías de manera flexible.

## Clase SistemaProductos

La clase `SistemaProductos` administra un árbol de productos y categorías utilizando nodos de la clase `NodoProducto`. Sirve para organizar productos en categorías jerárquicas, agregar nuevas categorías y productos, y buscar categorías dentro del árbol.

### Métodos

- **__init__()**
  - Inicializa el sistema con un nodo raíz llamado "Catálogo de Productos".

- **agregar_categoria(nombre: str, ruta: str = None)**
  - Agrega una nueva categoría al sistema.
  - Si `ruta` es `None` o una cadena vacía, la categoría se agrega como hija directa de la raíz.
  - Si se especifica una ruta (por ejemplo, `"Electrónica/Computadoras"`), la categoría se agrega como hijo de la última categoría de la ruta, creando las categorías intermedias si no existen.

- **buscar_nodo_categoria(nombre: str)**
  - Busca y retorna el nodo de la categoría cuyo nombre coincide con el argumento.
  - Si no se encuentra, retorna `None`.

- **agregar_producto(categoria: str, nombre: str, precio: float, stock: int)**
  - Agrega un producto como hijo de la categoría indicada.
  - Si la categoría no existe, muestra un mensaje de error.

### Funcionamiento

- El sistema permite construir una jerarquía de categorías y productos.
- Las categorías pueden anidarse unas dentro de otras.
- Los productos solo pueden agregarse como hijos de una categoría existente.
- La búsqueda de categorías se realiza por nombre, recorriendo todo el árbol.

---

## Lista de mejoras o revisiones

1. **Nombres duplicados:** Si hay dos categorías con el mismo nombre en diferentes ramas qué pasa? Claramente no deseado
2. **Eliminar categorías y productos:** Agregar métodos para eliminar categorías y productos.
3. **Listar productos/categorías:** Métodos para listar todos los productos de una categoría o todas las categorías hijas.
4. **Updatear producto:** Métodos para modificar el nombre, precio o stock de un producto.

### Extras
5. **Validar rutas:** validación de rutas.
6. **Serialización:** Métodos para guardar y cargar la estructura en archivos (por ejemplo, JSON).
7. **Control de stock:** Métodos para agregar/disminuir stock.

