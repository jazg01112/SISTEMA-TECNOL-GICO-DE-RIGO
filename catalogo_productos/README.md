# Catálogo de productos tecnológicos - Árbol binario de búsqueda

## Requisitos
- Python 3
- web.py
- SQLite3 (incluido en Python)

## Instalación en Windows / PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Si PowerShell bloquea la activación del entorno, ejecuta:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Abre en el navegador: http://localhost:8080

## Instalación en GitHub Codespaces / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Estructura MVC
- models: conexión SQLite, nodo y árbol binario de búsqueda.
- controllers: lógica para registrar, buscar, eliminar y consultar productos.
- views: páginas HTML sencillas.
- app.py: rutas y arranque del servidor.

## Clave del árbol
El ID del producto es la clave de ordenamiento:
- IDs menores van al subárbol izquierdo.
- IDs mayores van al subárbol derecho.
- El recorrido inorden muestra los productos ordenados por ID.

La base de datos se crea automáticamente al iniciar la aplicación.
