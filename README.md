# ASIX2WEB

Aplicación simple de gestión de correos (ASIR 2º).

## Requisitos
- Python 3.8+
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar
- Opción 1 (directo):

```bash
python app.py
```

- Opción 2 (con Flask CLI):

```bash
set FLASK_APP=appejercicio.py   # Windows
flask run
```

La app estará disponible en http://127.0.0.1:5000/ (redirige a `/getmail`).

## Notas
- Las plantillas están en `templates/` y los archivos estáticos en `static/`.
- Ignora `database.db` en el repositorio (está en `.gitignore`).
- `appejercicio.py` contiene la lógica principal de la aplicación.
