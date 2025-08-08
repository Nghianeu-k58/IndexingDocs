"""
Define router uploading file to indexing to database.
"""

from fastapi import (
    APIRouter,
    status,
    Depends,
    Form,
    File,
    UploadFile,
)
from typing import Annotated, List

from fastapi.responses import JSONResponse

from src.rag.core.logger import logger
from src.rag.file.models import DocsIndexingFields
from src.rag.dataaccess.migrations.elasticsearch.connection import (
    get_elastic_connection,
)
from src.rag.file.services import insert_doc

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("/")
async def upload_document(
    title: Annotated[str, Form(...)],
    key_words: Annotated[List[str], Form(...)],
    file: Annotated[UploadFile, File(...)],
    es_conn=Depends(get_elastic_connection),
):
    # preparing docs
    logger.info("Processing file ...")
    content = await file.read()
    doc_dict = {
        DocsIndexingFields.title: title,
        DocsIndexingFields.key_words: key_words,
        DocsIndexingFields.content: content.decode(),
    }

    res, msg = insert_doc(doc=doc_dict, es_conn=es_conn)
    if not res:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"msg": msg},
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "OK"})
