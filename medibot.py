
# import os
# import streamlit as st
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.chains import RetrievalQA
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import PromptTemplate
# from langchain_huggingface import HuggingFaceEndpoint
# from dotenv import load_dotenv


# # Load environment variables from .env file
# load_dotenv()


# # ✅ Load Hugging Face API Token (SECURE)
# HF_TOKEN = os.getenv("HF_TOKEN")  # Ensure this is set in your environment
# HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

# # Print to check (Remove this in production)
# print("API Token:", HF_TOKEN)  # This should print your token if loaded correctly

# # ✅ Ensure API token is set
# if not HF_TOKEN:
#     st.error("Hugging Face Token is missing! Set HF_TOKEN in your environment variables.")

# # ✅ FAISS vector store path
# DB_FAISS_PATH = "vectorstore/db_faiss"

# @st.cache_resource
# def get_vectorstore():
#     """Load FAISS vectorstore with embeddings"""
#     try:
#         embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#         db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
#         return db
#     except Exception as e:
#         st.error(f"Error loading FAISS index: {str(e)}")
#         return None

# def load_llm():
#     """Load Hugging Face model"""
#     if not HF_TOKEN:
#         return None  # Already handled by Streamlit error above

#     try:
#         return HuggingFaceEndpoint(
#             repo_id=HUGGINGFACE_REPO_ID,
#             temperature=0.5,
#             model_kwargs={"token": HF_TOKEN, "max_length": 200}
#         )
#     except Exception as e:
#         st.error(f"Error loading Hugging Face model: {str(e)}")
#         return None

# def set_custom_prompt():
#     """Define a custom prompt template"""
#     custom_prompt_template = """
#         Use the provided context to answer the user's question.
#         If you don't know the answer, just say so. Don't make up information.
#         Stick to the context provided.

#         Context: {context}
#         Question: {question}

#         Start the answer directly. No small talk.
#     """
#     return PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])

# def main():
#     """Main function for the Streamlit chatbot"""
#     st.title("Your AI Help Chatbot ")

#     # Store messages in session state
#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         st.chat_message(message['role']).markdown(message['content'])

#     # User input
#     prompt = st.chat_input("How Can Help You. Enter your question here...")

#     if prompt:
#         st.chat_message('user').markdown(prompt)
#         st.session_state.messages.append({'role': 'user', 'content': prompt})

#         try:
#             vectorstore = get_vectorstore()
#             if vectorstore is None:
#                 st.error("Failed to load the vector store")
#                 return

#             llm = load_llm()
#             if llm is None:
#                 return

#             # ✅ Load the retrieval-based QA chain
#             qa_chain = RetrievalQA.from_chain_type(
#                 llm=llm,
#                 chain_type="stuff",
#                 retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
#                 return_source_documents=True,
#                 chain_type_kwargs={'prompt': set_custom_prompt()}
#             )

#             # ✅ Get response
#             response = qa_chain.invoke({'query': prompt})
#             result = response["result"]
#            # source_documents = response.get("source_documents", [])

#             # ✅ Display response & source documents
#             #result_to_show = result + "\n\n**Source Docs:**\n" + str(source_documents)
#             st.chat_message('assistant').markdown(result)
#             st.session_state.messages.append({'role': 'assistant', 'content': result})

#         except Exception as e:
#             st.error(f"Error: {str(e)}")

# # Run the Streamlit app
# if __name__ == "__main__":
#     main()


import os
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vectorstore/db_faiss"

# Streamlit UI Configuration
st.set_page_config(page_title="AI Help Chatbot", page_icon="🤖", layout="wide")

# Sidebar
q
    st.title("🔍 AI Chatbot Settings")
    st.markdown("### ⚙️ Configuration")
    st.markdown(f"**Model:** `{HUGGINGFACE_REPO_ID}`")
    st.markdown("**Vector Store:** FAISS")
    st.markdown("---")
    st.markdown("### 🛠 Need Help?")
    st.markdown("Contact support at : [support@AI.com](mailto:support@AI.com)")
    st.markdown("---")
    st.markdown("🖥️ About AI")
    st.markdown(" Documentation : [About@AI.com](mailto:About@AI.com)")

# Load FAISS Vector Store
@st.cache_resource
def get_vectorstore():
    try:
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
        return db
    except Exception as e:
        st.sidebar.error(f"Error loading FAISS index: {str(e)}")
        return None

# Load Hugging Face Model
def load_llm():
    try:
        return HuggingFaceEndpoint(repo_id=HUGGINGFACE_REPO_ID, temperature=0.5, model_kwargs={"token": HF_TOKEN, "max_length": 200})
    except Exception as e:
        st.sidebar.error(f"Error loading model: {str(e)}")
        return None

# Custom Prompt
prompt_template = PromptTemplate(
    template="""
        Use the provided context to answer the user's question.
        If you don't know the answer, just say so. Don't make up information.
        Context: {context}
        Question: {question}
        Answer:
    """,
    input_variables=["context", "question"]
)

def main():
    st.title("🤖 AI Help Chatbot")
    st.write("Ask me anything and I'll try to help!")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    prompt = st.chat_input("Type your question here...")

    if prompt:
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        with st.spinner("Thinking..."):
            vectorstore = get_vectorstore()
            if vectorstore is None:
                st.error("Vectorstore failed to load.")
                return

            llm = load_llm()
            if llm is None:
                return

            qa_chain = RetrievalQA.from_chain_type(
                llm=llm,
                chain_type="stuff",
                retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                return_source_documents=True,
                chain_type_kwargs={'prompt': prompt_template}
            )

            response = qa_chain.invoke({'query': prompt})
            result = response.get("result", "No response generated.")
            
            st.chat_message('assistant').markdown(result)
            st.session_state.messages.append({'role': 'assistant', 'content': result})

if __name__ == "__main__":
    main()









