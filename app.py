import streamlit as st
import uuid
from dotenv import load_dotenv
import os
# from langfuse.callback import CallbackHandler

from src.components.pdf_loader import get_pdf_text, create_text_chunks
from src.components.vector_store import save_vector_store
from src.components.agents import create_agent

load_dotenv()

# lang_skey = os.environ["LANGFUSE_SECRET_KEY"]
# lang_pkey = os.environ["LANGFUSE_PUBLIC_KEY"]
# lang_host = os.environ["LANGFUSE_HOST"]

# #Initialize Langfuse CallbackHandler
# langfuse_handler = CallbackHandler(
#     public_key=lang_pkey,
#     secret_key=lang_skey,
#     host=lang_host,
#     session_id="Agentic RAG Pipeline",
#     trace_name="Agentic RAG Pipeline",
#     user_id="User"
# )

# st.set_page_config(page_title="Agentic RAG Chatbot")
# st.title("RAG Medical ChatBot")
st.markdown(
    """
    <h1>
        <img src="https://img.icons8.com/fluency/48/doctors-bag.png" width="40">
        RAG Medical ChatBot
    </h1>
    """,
    unsafe_allow_html=True
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = None

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

#Upload PDFs
with st.sidebar:
    st.header("Upload PDFs")

    pdf_docs = st.file_uploader(
        "Upload your PDF files",
        accept_multiple_files=True
    )

    if st.button("Process PDFs"):
        if pdf_docs:
            with st.spinner("Processing PDFs..."):

                # Extract text
                documents = get_pdf_text(pdf_docs)

                # Chunking
                text_chunks = create_text_chunks(documents)

                # Vector DB
                vector_store = save_vector_store(text_chunks)

                # Create LangGraph agent
                st.session_state.agent = create_agent(vector_store)

            st.success("Agent Ready 🚀")
        else:
            st.warning("Upload at least one PDF.")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.success("Chat cleared.")

#Cht history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Input to process
user_input = st.chat_input("Ask a question from your PDF")

if user_input:

    if st.session_state.agent is None:
        st.warning("Please upload and process PDFs first.")
    else:
        # Store user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            with st.chat_message("assistant"):

                response_container = st.empty()

                # ✅ Correct LangGraph call
                response = st.session_state.agent.invoke(
                    {
                        "messages": [
                            {"role": "user", "content": user_input}
                        ]
                    },
                    config={
                        "configurable": {
                            "thread_id": st.session_state.thread_id
                        },
                        "callbacks": [langfuse_handler]
                    }
                )


                final_message = response["messages"][-1]
                full_response = final_message.content

                response_container.markdown(full_response)

            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

# # Apply guardrails
# safe_response = apply_guardrails(full_response)
# response_container.markdown(safe_response)







