"""
Define to app registers for rag services.
"""

from fastapi import FastAPI, Response, status
from .api import api_routers

DESCRIPTION = """
Welcome to LocalRAG API documentation!
Here you will able to discover all of the ways you can interact with the LocalRAG API.
Happy codeing.
"""

app = FastAPI(
    title="LocalRag document indexing service.",
    description=DESCRIPTION,
    docs_url="/api/docs",
    redoc_url="/api/schemas",
)


app.include_router(api_routers)


@app.get("/health-check", tags=["Health Check"])
def health_check():
    return Response(status_code=status.HTTP_200_OK, content="OK")
