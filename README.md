# Challenge N5! Automatizacion de Netflix

## Descripción

Este proyecto contiene scripts de automatización para realizar pruebas en la interfaz de usuario de Netflix. Utiliza Selenium con Python para interactuar con elementos de la página y automatizar pruebas de la interfaz de usuario.

## Estructura del Proyecto
- `pages/`: Contiene los scripts de Selenium que interactúan con las páginas web de Netflix.
- `tests/`: Directorio con los casos de prueba.
- `utils/`: Herramientas y utilidades para apoyar las pruebas.
- `reports/`: Ubicación para los informes generados por las pruebas.
- `.gitignore`: Archivo para especificar los archivos desatendidos en git.
- `conftest.py`: Configuraciones iniciales para las pruebas con pytest.
- `.pytest_cache`: Cache generado por pytest para optimizar la ejecución de pruebas.

## Requisitos
- Integrated development environment (IDE) Ejemplo: Visual Studio Code, Pycharm o similares
- PIP
- Python 3.x
- Selenium
- pytest

## Instrucciones para instalar y configurar los requisitos
- Descargar Visual Studio Code

1. Visita la página oficial de Visual Studio Code: https://code.visualstudio.com/
2. Elige la versión adecuada para tu sistema operativo (Windows, macOS, Linux).
3. Descarga e instala el programa siguiendo las instrucciones en pantalla.

- Configurar Visual Studio Code

1. Al abrir Visual Studio Code por primera vez, puedes personalizar el tema y otras configuraciones según tus preferencias.
2. Puedes instalar extensiones útiles como Python o Git desde el panel de extensiones en el lado izquierdo.

- Descargar e instalar Python 3.x

1. Ve a la página oficial de Python: https://www.python.org/downloads/
2. Descarga la versión de Python 3.x que prefieras.
3. Instalar Python
4. Ejecuta el instalador descargado.
5. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
6. Sigue las instrucciones en pantalla para completar la instalación.

- Instalar PIP

PIP viene instalado por defecto con Python 3.4 y versiones posteriores. 

Si necesitas instalarlo o actualizarlo ve al siguiente link de la documentacion: https://pip.pypa.io/en/stable/installation/

> [!IMPORTANT]
> ## Notas Adicionales
> 
> Asegúrate de tener permisos de administrador si es necesario durante las instalaciones.
> 
> Después de instalar Python y PIP, puedes verificar sus versiones ejecutando python --version y pip --version en la terminal.
> 
> Si encuentras algún problema durante la instalación, revisa la documentación oficial o foros de la comunidad para soluciones específicas.

## Instalación
Para instalar las dependencias del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

> [!IMPORTANT]
> ## Ejecución de Pruebas
> Para ejecutar las pruebas y recibir un reporte html, utiliza el siguiente comando desde tu terminal (Windows):
>
>  ```bash
> pytest tests/netflix_home.py --html=reports/informe.html (Con este caso iremos al link indicado en la documentacion)

> pytest tests/netflix_home_ar.py --html=reports/informe.html (Con este caso iremos al link redirigido a Netflix Argentina)



>  ```
>  El reporte correspondiente se guardara en la carpeta `reports/` bajo el nombre: `informe.html`

> [!NOTE]
>
> ## Contribuciones
> Para contribuir con el proyecto, por favor envia tus pulls requests a la rama principal.





