
Aplicación en Python con estructura modular y lista para desplegar en entornos productivos gracias a **Docker** y **docker-compose**.  
Incluye una interfaz basada en plantillas y un backend ligero en Python, ideal como punto de partida para proyectos web o demostraciones rápidas.

Características
- Backend en Python (Flask u otro framework ligero).  
- Plantillas HTML listas para personalizar.  
- Contenedorización con **Docker** y orquestación con **docker-compose**.  
- Dependencias definidas en `requirements.txt`.  
- Fácil de extender y adaptar a tus necesidades.

Instalación

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/DaoVega/python-app-LENMOPRO.git
cd python-app-LENMOPRO
```
Instala las dependencias (si deseas ejecutarlo sin Docker):
pip install -r requirements.txt

Ejecución con Docker
Este proyecto está listo para ejecutarse en contenedores.

Asegúrate de tener instalado Docker y docker-compose
Desde la raíz del proyecto, corre:
docker-compose up --build

Accede a la aplicación en tu navegador en el puerto configurado.

Personaliza las rutas, lógica y vistas según tus necesidades.

Modifica las plantillas en app/templates/ para ajustar el frontend
