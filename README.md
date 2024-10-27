
# Evluación Django Developer
Este manual tiene como objetivo ayudar a cualquier persona a desplegar el proyecto en una nueva máquina. Siga estos pasos para instalar y ejecutar el proyecto correctamente. 




## Instalacion

Este manual tiene como objetivo ayudar a cualquier persona a desplegar el proyecto en una nueva máquina. Siga estos pasos para instalar y ejecutar el proyecto correctamente.

- Python (versión 3.8 o superior).
- PostgreSQL (Opcional): Este paso es opcional, dado que esta trabajando con el SQLite.
- Redis o Memurai: * Recuerda que lo puedes ejecutar a nivel administrativo, por comando CMD. Para otros sistemas operativos, puedes instalar Redis desde Redis.io.

Clonar el proyecto
```bash
git remote add origin https://github.com/angelxxrojo/pt_ordermanage.git
cd orders_project
```
Crear y Activar un Entorno Virtual
```bash
python -m venv manage_order_env
# Para Windows
manage_order_env\Scripts\activate
# Para Linux/Mac
source manage_order_env/bin/activate
```
Instalar Requerimientos
```bash
pip install -r requirements.txt
```

Create un super usuario
```bash
python manage.py createsuperuser
```

## Deployment

Para despliegue de aplicativo

```bash
  python manage.py runserver
```

Si tienes el memurai
```bash
memurai.exe # Para Windows usando Memurai
```
Si tienes el Redis
```bash
redis-server # Para otros sistemas operativos usando Redis
```
Usar el Celery
```bash
celery -A orders_project worker --loglevel=info -P solo
```

Para Acceder a la vista administrativa

Visita http://127.0.0.1:8000/admin/



## API Reference

#### Insertar datos para las ordenes

```http
  //127.0.0.1:8000/api/create-order/item_id=${item_id}&quantity=${quantity}&customer=${customer}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `item_id` | `number` | **Required** |
| `quantity` | `number` | **Required** |
| `customer` | `string` | **Required** |

Respuesta: 

"message": "Order created successfully",
"order_id": ${order_id}
