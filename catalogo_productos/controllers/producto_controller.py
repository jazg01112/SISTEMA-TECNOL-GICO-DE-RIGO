import web
from models import database
from models.arbol_binario import ArbolBinario

render = web.template.render("views/", base="layout")

class ProductoController:
    def __init__(self):
        database.crear_tabla()
        self.arbol = ArbolBinario()

        # Recupera los productos guardados y reconstruye el árbol.
        for producto in database.obtener_productos():
            self.arbol.insertar(producto)

    def inicio(self):
        productos = self.arbol.recorrido_inorden()
        return render.index(productos, "")

    def formulario(self):
        return render.nuevo("")

    def guardar(self, datos):
        try:
            id_producto = int(datos.id)
            nombre = datos.nombre.strip()
            categoria = datos.categoria.strip()
            marca = datos.marca.strip()
            precio = float(datos.precio)
            existencia = int(datos.existencia)

            if not nombre or not categoria or not marca:
                return render.nuevo("Todos los campos son obligatorios.")
            if precio < 0 or existencia < 0:
                return render.nuevo("El precio y la existencia no pueden ser negativos.")

            producto = (id_producto, nombre, categoria, marca, precio, existencia)

            # Primero se guarda en SQLite y después se agrega al árbol.
            database.insertar_producto(producto)
            self.arbol.insertar(producto)

            raise web.seeother("/")
        except ValueError as error:
            mensaje = str(error)
            if "Ya existe" in mensaje:
                return render.nuevo(mensaje)
            return render.nuevo("Verifica los datos: el ID, precio y existencia deben ser números.")
        except Exception as error:
            if isinstance(error, web.HTTPError):
                raise
            return render.nuevo("No se pudo guardar. Comprueba que el ID no esté repetido.")

    def buscar(self, id_texto):
        try:
            id_producto = int(id_texto)
        except ValueError:
            return render.resultado(None, "Escribe un ID numérico.")

        producto = self.arbol.buscar(id_producto)
        if producto is None:
            return render.resultado(None, "No se encontró un producto con ese ID.")
        return render.resultado(producto, "")

    def eliminar(self, id_texto):
        try:
            id_producto = int(id_texto)
        except ValueError:
            raise web.seeother("/")

        producto = self.arbol.buscar(id_producto)
        if producto is not None:
            database.eliminar_producto(id_producto)
            self.arbol.eliminar(id_producto)

        raise web.seeother("/")
