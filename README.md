# tercerpre-entregaGarcia
# Proyecto EduRead

Este proyecto es una aplicación web desarrollada con Django y Bootstrap. Proporciona información sobre cursos, entregables, profesores y estudiantes en el contexto de la plataforma educativa de EduRead.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual.
3. Instala las dependencias del proyecto ejecutando el comando:
pip install -r requirements.txt
4. Realiza las migraciones de la base de datos con el comando:
python manage.py migrate
5. Inicia el servidor de desarrollo local con el comando:
python manage.py runserver
6. Accede a la aplicación en tu navegador web mediante la URL `http://localhost:8000`.

## Estructura del proyecto

- La carpeta `Proyecto1` contiene la configuración principal del proyecto, que no será utilizada en esta ocasión.
- La carpeta `AppCoder` contiene la lógica de la aplicación web.
- La carpeta `templates` contiene las plantillas HTML utilizadas para las páginas.
- La carpeta `static` contiene los archivos estáticos como CSS, JavaScript e imágenes.

## Orden recomendado para probar las funcionalidades

1. Navega a la página http://127.0.0.1:8000/AppCoder/inicio/
2. Explora las diferentes secciones del sitio que se muestran en el navbar: cursos, entregables, estudiantes y profesores.
3. Registra un nuevo estudiante, profesor, entregable y curso.
4. Verifica que los datos se guarden correctamente en la base de datos, por medio del boton "buscar".
5. Comprueba que los iconos de las redes sociales te redirijan a las respectivas páginas externas al hacer clic en ellos.
6. Puedes navegar por medio del footer hacia las distintas secciones de la web.
7. Asegúrate de que el diseño y estilo de la aplicación se vean correctamente en diferentes dispositivos y tamaños de pantalla.
