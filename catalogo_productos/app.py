import web
from controllers.producto_controller import ProductoController

urls = (
    "/", "Inicio",
    "/nuevo", "Nuevo",
    "/buscar", "Buscar",
    "/eliminar", "Eliminar",
)

controller = ProductoController()

class Inicio:
    def GET(self):
        return controller.inicio()

class Nuevo:
    def GET(self):
        return controller.formulario()
    def POST(self):
        datos = web.input()
        return controller.guardar(datos)

class Buscar:
    def GET(self):
        datos = web.input(id="")
        return controller.buscar(datos.id)

class Eliminar:
    def POST(self):
        datos = web.input()
        return controller.eliminar(datos.id)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
