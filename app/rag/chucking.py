from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.logger import get_logger

logger = get_logger(__name__)

def splitDocuments(docs: list[Document], *, CHUNK_SIZE, CHUNK_OVERLAP) -> list[Document]:
    logger.info("Chunking documents")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
        add_start_index=True,
    )
    return splitter.split_documents(docs)