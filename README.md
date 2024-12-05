# myPokeAPI Project

Este proyecto utiliza datos de la la pagina **[PokeAPI.co](https://pokeapi.co/)** para crear una solución completa que incluye la extracción, transformación y carga de datos (ETL), el desarrollo de una API RESTful, y una aplicación web para visualizar la información.

## Tecnologías utilizadas

- MySQL
- Python con Flask
- SQLAlchemy
- Javascript con Vite + React.js
- TailwindCSS
- Material UI

## Configuracion del Backend (Flask)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto:

Sobre la carpeta `/be`
- Ejecuta el siguiente comando para acceder al directorio del backend
    ```sh
    cd .\be\
    ```
- Crear un virtual Enviorement en la raiz de la ruta con el comando
    ```sh
    python -m venv nombre_del_venv
    ```
- Situarse sobre la ruta del Virtual Enviorement con el comando
    ```sh
    .\nombre_del_venv\Scripts\activate
    ```
- Instalar las dependencias del proyecto Flask con el comando
    ```sh
    pip install -r .\requirements.txt
    ```
- Cree un archivo `.env` en la raíz del proyecto con la siguiente estructura:
    ```sh
    DB_CONN = "mysql+pymysql://user:password@host:port/mypokeapi"
    # Reemplaza user, password, host y port según tu configuración de MySQL.
    ```
> De ser necesario, borrar la carpeta migrations (solo si no le corre la migracion bien).
- Ejecuta el siguiente comando para preparar la migracion.
    ```sh
    flask db init
    ```
- Ejecuta el siguiente comando para correr la migracion.
    ```sh
    flask db migrate
    ```
- Ejecuta el siguiente comando para actualizar los datos migrados.
    ```sh
    flask db upgrade
    ```
- Ejecuta el siguiente comando para extraer los datos de la pagina de **[PokeAPI.co](https://pokeapi.co/)** e insertarlos a la base de datos.
    ```sh
    flask seed
    ```
- Ejecuta el siguiente comando para iniciar el proyecto Flask.
    ```sh
    py app.py
    ```
- Ya se debería tener el Backend ejecutado.

## Configuracion del Frontend (Vite + React.js)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto:

Sobre la carpeta `/fe`
- Ejecuta el siguiente comando para acceder al directorio del frontend.
    ```sh
    cd .\fe\
    ```
- Crear un archivo `.env` en la raíz del proyecto con la siguiente estructura:
    ```sh
    VITE_BE_URL=your_backend_url_here
    # Reemplaza la URL con la que obtuviste al ejecutar el backend.
    ```
- Ejecuta el siguiente comando para instalar todas las dependencias node modules.
    ```sh
    npm i
    ```
- Ejecuta el siguiente comando para iniciar el proyecto Vite + React.js.
    ```sh
    npm run dev
    ```
- Ya se debería tener el Frontend ejecutado.

## Problemas comunes

Si no puedes activar el Enviorement del Python y tienes un error con el ExecutionPolicy
- Debe ejecutar uno de los siguientes comandos en el Powershell:

    ```sh
    # Escoja cualquiera de los siguientes
    Set-ExecutionPolicy Unrestricted -Scope CurrentUser
    Set-ExecutionPolicy Unrestricted -Scope Process
    ```
- Luego puede volver a reestablecerlo con el siguiente comando
    ```sh
    set-executionpolicy remotesigned
    ```
- Ahora solamente debe de utilizar en la terminal de visual code lo siguiente
    ```sh
    ./activate
    ```

## ENLACES DE LOS DOCUMENTOS

- **[Enlace del documento](https://utpac-my.sharepoint.com/:b:/g/personal/rafael_chung_utp_ac_pa/EdKbnyhU85ZItu9Fm5Yg9H8Bwng1WAuUzOSxTRAWL5A5Ng?e=kLME2q)**
- **[Enlace de la presentacion](https://utpac-my.sharepoint.com/:p:/g/personal/rafael_chung_utp_ac_pa/EbEsPVXJvr5PnwQwgDPeiRAB2w4rSk-gYPsPh03vAcj0nw?e=bBTTar)**