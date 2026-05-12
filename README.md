# MI code

Coleccion de ejercicios y agentes en Python del curso LangGraph. Incluye agentes basicos, agentes con herramientas, y un agente tipo profesor con RAG.

## Estructura

- Agent 1-5: ejercicios base.
- AI Agent 1-5: agentes con herramientas y logs.
- Proyect/Profesor.py: agente profesor generico con RAG sobre documentos PDF.

## Requisitos

- Python 3.10+ recomendado
- Paquetes principales (ver abajo)

## Instalacion rapida

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Si no tienes un requirements.txt actualizado, instala lo basico:

```powershell
pip install langchain langchain-community langchain-openai langchain-chroma chromadb python-dotenv
```

## Variables de entorno

Crea un archivo .env en la carpeta "MI code" con tu clave:

```
OPENAI_API_KEY=tu_api_key
```

## Como correr el agente profesor

```powershell
.\.venv\Scripts\Activate.ps1
python "Proyect\Profesor.py"
```

Cuando lo ejecute, te pedira rutas de PDFs separadas por coma. Ejemplo:

```
"C:\Users\Peter\Downloads\resumen ing de datos 2 parcial 1.pdf"
```

Luego puedes hacer preguntas en consola. Escribe `exit` o `quit` para salir.

## Notas

- El agente crea un vectorstore en `chroma_db` dentro del directorio donde se ejecuta.
- Si cambia el conjunto de PDFs, se recomienda borrar `chroma_db` para regenerar el indice.
