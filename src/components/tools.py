from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

def create_retriever_tool(vector_store):

    @tool
    def retrieve_docs(query: str) -> str:
        """
        Use this tool to retrieve relevant information strictly from the uploaded PDF documents.

        Only use this tool when:
        - The question is about the uploaded documents.
        - The answer requires document-specific knowledge.

        Do NOT use for general knowledge questions.
        """
        docs = vector_store.similarity_search(query, k=3)
        return "\n\n".join([doc.page_content for doc in docs])

    return retrieve_docs

def create_web_tool():

    search = TavilySearchResults(max_results=3)

    @tool
    def web_search(query: str) -> str:
        """
        Use this tool to search the web for up-to-date information.
        """
        return search.invoke({"query": query})

    return web_search