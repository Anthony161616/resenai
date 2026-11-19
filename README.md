# ReseñAI

Agente de inteligencia artificial que analiza reseñas de clientes de restaurantes, detecta críticas urgentes y genera un informe semanal.
Proyecto del curso **Taller de Proyectos 1** (Universidad Continental) · Autor: Vargas Yanarico, Ewer Anthony.

## Estructura
| Carpeta | Contenido |
|---|---|
| `backend/` | Lógica del sistema (validaciones, API y servicios) |
| `frontend/` | Interfaces P1 a P5 |
| `database/` | Script SQL de las 10 tablas, consultas CRUD y creación de una base local de prueba |
| `docs/` | Documentos del curso (PA1 y PA2) |
| `tests/` | Pruebas automáticas |

## Cómo preparar el entorno
```
python -m venv venv
venv\Scripts\activate          (Windows)   |   source venv/bin/activate   (Linux/Mac)
pip install -r requirements.txt
python verificar_entorno.py
python database/crear_bd_local.py
python -m unittest discover -s tests -v
```

## Ramas y commits
- `main`: versión estable. `develop`: integración. `feature/HU-xx`: una rama por historia de usuario.
- Mensajes de commit con la historia, por ejemplo: `HU-01: validar correo y contraseña`.
- Las claves y contraseñas van en un archivo `.env` (no se sube). Use `.env.example` como modelo.

## Estado
Release 1 (HU-01 a HU-05): en preparación. El plan completo está en el PA2.
