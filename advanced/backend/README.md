### README.md


# Money Tracker API

## Descripción

Money Tracker API es una aplicación diseñada para gestionar transacciones financieras, cuentas de usuario y categorías de transacciones. Este proyecto se ha creado para enseñar los fundamentos del desarrollo Fullstack en una clase.

## Características

- Gestión de usuarios
- Gestión de cuentas
- Gestión de transacciones
- Gestión de tipos y categorías de transacciones
- Autenticación y autorización mediante JWT
- Middleware para manejo de errores y seguridad

## Estructura del Proyecto

backend_money/
├── config/
│   ├── __init__.py
│   ├── database.py
├── middlewares/
│   ├── __init__.py
│   ├── error_handler.py
│   ├── jwt_bearer.py
├── models/
│   ├── __init__.py
│   ├── account.py
│   ├── transaction.py
│   ├── transaction_category.py
│   ├── transaction_type.py
│   ├── user.py
├── routers/
│   ├── __init__.py
│   ├── account.py
│   ├── auth.py
│   ├── transaction.py
│   ├── transaction_category.py
│   ├── transaction_type.py
│   ├── user.py
├── schemas/
│   ├── __init__.py
│   ├── account.py
│   ├── transaction.py
│   ├── transaction_category.py
│   ├── transaction_type.py
│   ├── user.py
├── services/
│   ├── __init__.py
│   ├── transaction.py
│   ├── user.py
├── utils/
│   ├── jwt_manager.py
├── main.py
├── README.md
├── requirements.txt
```

## Instalación

1. Clonar el repositorio:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd backend_money
   ```

2. Crear un entorno virtual y activar:
   ```sh
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
   ```

3. Instalar las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno:
   Crear un archivo `.env` en la raíz del proyecto y agregar las siguientes variables:
   ```sh
   SECRET_KEY=tu_clave_secreta
   DATABASE_URL=sqlite:///./test.db  # O la URL de tu base de datos
   ```

5. Inicializar la base de datos:
   ```sh
   python main.py
   ```

## Uso

1. Ejecutar la aplicación:
   ```sh
   uvicorn main:app --reload
   ```

2. Acceder a la documentación automática generada por FastAPI:
   - Documentación interactiva (Swagger): `http://127.0.0.1:8000/docs`
   - Documentación alternativa (Redoc): `http://127.0.0.1:8000/redoc`

## Endpoints Principales

### Autenticación
- `POST /login`: Iniciar sesión y obtener un token JWT.

### Usuarios
- `GET /users/`: Obtener todos los usuarios.
- `POST /users/`: Crear un nuevo usuario.
- `GET /users/{id}`: Obtener un usuario por ID.
- `PUT /users/{id}`: Actualizar un usuario.
- `DELETE /users/{id}`: Desactivar un usuario.

### Cuentas
- `GET /accounts/`: Obtener todas las cuentas.
- `POST /accounts/`: Crear una nueva cuenta.
- `GET /accounts/{id}`: Obtener una cuenta por ID.
- `PUT /accounts/{id}`: Actualizar una cuenta.
- `DELETE /accounts/{id}`: Eliminar una cuenta.

### Transacciones
- `GET /transactions/`: Obtener todas las transacciones.
- `POST /transactions/`: Crear una nueva transacción.
- `GET /transactions/{id}`: Obtener una transacción por ID.
- `PUT /transactions/{id}`: Actualizar una transacción.
- `DELETE /transactions/{id}`: Eliminar una transacción.
- `GET /transactions/user/{user_id}`: Obtener transacciones por usuario.
- `GET /transactions/user/{user_id}/filter`: Filtrar transacciones por usuario.

## Contribuir

1. Hacer un fork del proyecto.
2. Crear una nueva rama (`git checkout -b feature/nueva-feature`).
3. Realizar los cambios necesarios y commit (`git commit -am 'Agrega nueva feature'`).
4. Push a la rama (`git push origin feature/nueva-feature`).
5. Crear un nuevo Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. 
