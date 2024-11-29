# myPokeAPI Project by Rchungye

Este proyecto utiliza datos de la la pagina **[PokeAPI.co](https://pokeapi.co/)** para crear una solución completa que incluye la extracción, transformación y carga de datos (ETL), el desarrollo de una API RESTful, y una aplicación web para visualizar la información.

## Tecnologías

- MySQL
- Python con Flask
- SQLAlchemy
- Javascript con Vite + React.js
- TailwindCSS
- Material UI

## Configuracion del Backend (Flask)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto:

Sobre la carpeta /be
- Ejecutar el comando **cd .be** para acceder al directorio del backend.
- Crear un virtual Enviorement en la raiz de la ruta con el comando **python -m venv nombre_del_venv**
- Situarse sobre la ruta del Virtual Enviorement con el comando **nombre_del_venv/Scripts/activate**
- Instalar las dependencias del proyecto Flask con el comando **pip install -r requirements.txt**
- De ser necesario, borrar la carpeta migrations (solo si no le corre la migracion bien).
- Ejecutar el comando **flask db init** para preparar la migracion.
- Ejecutar el comando **flask db migrate** para correr la migracion.
- Ejecutar el comando **flask db upgrade** para actualizar los datos migrados.
- Ejecutar el comando **flask seed** para extraer los datos de la pagina de **[PokeAPI.co](https://pokeapi.co/)** e ir insertandolos a la base de datos.
- Correr el comando **py app.py** para iniciar el proyecto Flask
- Ya se debería tener el Backend ejecutado.

## Configuracion del Frontend (Vite + React.js)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto:

Sobre la carpeta /fe
- Ejecutar el comando **cd .fe** para acceder al directorio del frontend.
- Correr el comando **npm i** para instalar todas las dependencias node modules.
- Correr el comando **npm run dev** para preparar los componentes Vite + React.js y permanecer escuchando los cambios sobre los componentes de React.js
- Ya se debería tener el Frontend ejecutado.

### Problemas comunes

Si no puedes activar el Enviorement del Python y tienes un error con el ExecutionPolicy debe ejecutar uno de los siguientes comandos en el Powershell:
- **Set-ExecutionPolicy Unrestricted -Scope CurrentUser**
- **Set-ExecutionPolicy Unrestricted -Scope Process**
- Luego puede volver a reestablecerlo con el siguiente comando **set-executionpolicy remotesigned**
- Ahora solamente debe de utilizar en la terminal de visual code lo siguiente **./activate**