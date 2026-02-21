from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate

from src.components.llm import load_llm


CUSTOM_PROMPT_TEMPLATE = """You are a helpful medical assistant.

Answer the following medical question in 2-3 lines maximum
using only the information provided in the context.

If the answer is not present in the context,
say "The information is not available in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

def set_custom_prompt():
    return PromptTemplate(
        template=CUSTOM_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )


def create_qa_chain(vector_store):

    llm = load_llm()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
        memory=memory,
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": set_custom_prompt()}
    )

    return qa_chain
