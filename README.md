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
- Python 3.x
- Selenium
- pytest

## Instalación
Para instalar las dependencias del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

> [!IMPORTANT]
> ## Ejecución de Pruebas
> Para ejecutar las pruebas y recibir un reporte html, utiliza el siguiente comando:
>
>  ```bash
>  pytest tests/test_netflix_home.py --html=reports/informe.html
>  ```
>  El reporte correspondiente se guardara en la carpeta `reports/` bajo el nombre: `informe.html`

> [!NOTE]
>
> ## Contribuciones
> Para contribuir con el proyecto, por favor envia tus pulls requests a la rama principal.





