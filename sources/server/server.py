from flask import Flask, jsonify, request
from flask_cors import CORS

import os
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

documents = []
for file in os.listdir("docs"):
    if file.endswith(".pdf"):
        pdf_path = "./docs/" + file
        loader = PyPDFLoader(pdf_path)
        documents.extend(loader.load())
    elif file.endswith('.docx') or file.endswith('.doc'):
        doc_path = "./docs/" + file
        loader = Docx2txtLoader(doc_path)
        documents.extend(loader.load())
    elif file.endswith('.txt'):
        text_path = "./docs/" + file
        loader = TextLoader(text_path)
        documents.extend(loader.load())


# Split the documents into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
documents = text_splitter.split_documents(documents)

# Convert the document chunks to embedding and save them to the vector store
vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="./data")
vectordb.persist()

# create our Q&A chain
document_qa = ConversationalRetrievalChain.from_llm(
    ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
    retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
    return_source_documents=True,
    verbose=False
)

chat_history = []
app = Flask(__name__)
cors = CORS(app, origins=['http://localhost:3000'])


@app.route('/api/chat', methods=['POST'])
def api():
    if request.method == 'POST':
        try:
            data = request.get_json()
            query = data.get('message')

            result = document_qa.invoke({"question": query, "chat_history": chat_history})
            chat_history.append((query,result["answer"]))
            return jsonify({'message': result["answer"]})
        
        except Exception as e:
            print(f"Error processing request: {e}")
            return jsonify({'error': 'Error processing request'}), 500

if __name__ == '__main__':
    app.run(port=5000)
