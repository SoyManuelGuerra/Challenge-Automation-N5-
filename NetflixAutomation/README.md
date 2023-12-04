# Marco de Pruebas Automatizadas con Sleenium - Por Manuel Guerra

Este repositorio contiene un marco de pruebas automatizadas diseñado para la aplicación web Finnegans, utilizando Selenium con Python para automatizar las acciones del navegador.

Descripción de los Componentes

drivers/: Contiene los WebDriver para diferentes navegadores. Por ejemplo, ChromeDriver para Google Chrome. Estos drivers son necesarios para que Selenium interactúe con el navegador.

pages/: Aquí se implementa el Page Object Model. Cada archivo representa una página específica de la aplicación web (en este caso, Netflix). Por ejemplo, HomePage.py contendría todos los localizadores y métodos para interactuar con la página de inicio de Netflix.

BasePage.py: Una clase base que puede contener funcionalidades comunes a todas las páginas, como inicialización del driver y métodos comunes (por ejemplo, navigate_to(url)).
tests/: Contiene los scripts de prueba. Cada archivo de prueba se enfoca en una página o funcionalidad específica de la aplicación web. Estos scripts usarán los objetos de página definidos en el directorio pages/.

utils/: Utilizado para código de soporte como utilidades de manejo de configuraciones, métodos de ayuda, etc.

reports/: Directorio para almacenar informes generados por las ejecuciones de pruebas. Herramientas como Allure pueden colocar aquí sus informes.

.gitignore: Este archivo se utiliza para indicar a Git qué archivos o directorios ignorar en el control de versiones, como __pycache__, archivos de configuración personal, etc.

requirements.txt: Un archivo de texto que lista todas las dependencias del proyecto, como selenium, para que puedan instalarse fácilmente en un nuevo entorno utilizando pip install -r requirements.txt.