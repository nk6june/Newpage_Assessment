
import os
from pypdf import PdfReader
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from src.common.logger import get_logger
from src.common.custom_exception import CustomException

from src.config.config import CHUNK_SIZE,CHUNK_OVERLAP

logger = get_logger(__name__)

def get_pdf_text(pdf_docs):
    try:
        if not pdf_docs:
            raise CustomException("No PDF documents were found")
        
        logger.info(f"Extracting text from {len(pdf_docs)} PDF documents")

        documents = [] 
        for pdf in pdf_docs:
            logger.info(f"Reading PDF file: {pdf}")

            pdf_reader = PdfReader(pdf)
            text = ""
           
            for page in pdf_reader.pages:
                text += page.extract_text()

            documents.append(Document(page_content=text))
                
    except Exception as e:
        error_message = CustomException("Failed to extract text from PDFs", e)
        logger.error(str(error_message))
        raise error_message
    return documents


def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents were found")
        
        logger.info(f"Splitting {len(documents)} documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE,chunk_overlap=CHUNK_OVERLAP)

        text_chunks = text_splitter.split_documents(documents)

        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_message = CustomException("Failed to generate chunks" , e)
        logger.error(str(error_message))
        return []


