# Modulo6

Este repositorio contiene ejemplos utilizando las bibliotecas **Flask**, **Streamlit** y **FastAPI**. El objetivo es proporcionar una guía práctica para empezar a trabajar con cada una de estas herramientas de desarrollo
web en Python.

## Bibliotecas Incluidas

*   **Flask:** Un microframework web flexible y versátil. Los ejemplos cubren conceptos básicos como rutas, plantillas, formularios y APIs.
*   **Streamlit:**  Una herramienta para crear aplicaciones web interactivas de datos con facilidad.  Los ejemplos muestran cómo crear dashboards, visualizaciones y aplicaciones basadas en datos.
*   **FastAPI:** Un framework web de alto rendimiento para construir APIs con Python, con un enfoque en la velocidad y la facilidad de uso.  Los ejemplos exploran la definición de endpoints, validación de datos y serialización.

## Estructura del Repositorio

La estructura del repositorio es la siguiente:

```
.
├── fastapi_examples
│   ├── 01_hello_world.py
│   ├── 02_generate.py
│   ├── 03_path.py
│   ├── 04_post.py
│   ├── 05_events.py
│   ├── 06_bg_task.py
│   ├── 07_chart.py
│   ├── 08_webscrap_gui.py
│   ├── sam2_api.py
│   ├── sam2_gui.py
│   ├── sync.py
│   └── webscrap_llm.py
├── flask_examples
│   └── webapp
│       ├── main.py
│       ├── static
│       │   ├── css
│       │   │   └── styles.css
│       │   ├── images
│       │   │   ├── 1.jpg
│       │   │   ├── 2.jpg
│       │   │   ├── 3.jpg
│       │   │   └── 4.jpg
│       │   └── js
│       │       └── code.js
│       └── templates
│           └── template.html
├── images
│   ├── dr_mariano_rivera.jpg
│   ├── elephant1.jpg
│   ├── elephant2.jpg
│   └── tiger.jpg
├── README.md
├── requirements-dl.txt
├── requirements.txt
└── streamlit_examples
    ├── main.py
    └── pages
        ├── 01_hello_world.py
        ├── 02_write.py
        ├── 03_write_stream.py
        ├── 04_widgets.py
        ├── 05_image.py
        ├── 06_camera.py
        ├── 07_charts.py
        ├── 08_map_chart.py
        ├── 08_maps_cache.py
        ├── 09_chart_pyploy.py
        ├── 10_cache.py
        ├── 11_cache_resources.py
        ├── 12_session_state.py
        ├── 13_chat_ollama.py
        ├── 14_heatmap.py
        ├── 15_live_camera.py
        └── 16_login.py
```

## Requisitos

Para ejecutar los ejemplos, necesitarás crear un ambiente (como conda o venv) con Python 3.11.  Además, necesitarás instalar las dependencias:

*   **Web**: `pip install -r requirements.txt`
*   **DL**: `pip install -r requirements-dl.txt`



## Ejecución de los Ejemplos

Se recomienda guardar cada ejemplo en su propia carpeta: ***`fastapi_examples/`***, ***`flask_examples/`*** y ***`streamlit_examples/`***.

Para ejecutar un ejemplo, navega a la carpeta principal **Modulo6**:

*   **Flask:** *`flask --app flask_examples/webapp/01_hello.py run --debug`* (o el nombre del archivo **.py** principal)
*   **Streamlit:** *`streamlit run streamlit_examples/pages/01_hello_world.py`* (o el nombre del archivo **.py** principal)
*   **FastAPI:** *`fastapi run fastapi_examples/01_hello.py --port 8080`* (o el nombre del archivo **.py** principal)


## Contacto

Si tienes alguna pregunta o comentario, puedes contactar a [octavio.renteria@cimat.mx](mailto:octavio.renteria@cimat.mx).
