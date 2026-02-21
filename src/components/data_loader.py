import os
from src.components.pdf_loader import get_pdf_text,create_text_chunks
from src.components.vector_store import save_vector_store
from src.config.config import DB_FAISS_PATH

from src.common.logger import get_logger
from src.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("MAking the vectorstore....")
        
        documents = get_pdf_text()

        text_chunks = create_text_chunks(documents)

        save_vector_store(text_chunks)

        logger.info("Vectorstore created sucesfully....")

    except Exception as e:
        error_message = CustomException("Faialedd to create vectorstore",e)
        logger.error(str(error_message))


if __name__=="__main__":
    process_and_store_pdfs()