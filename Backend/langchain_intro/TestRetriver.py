# # Test.py

# import dotenv
# from langchain_community.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
# import os

# # Đường dẫn đến thư mục lưu trữ cơ sở vector
# REVIEWS_CHROMA_PATH = "chroma_data"

# # Load biến môi trường từ file .env
# dotenv.load_dotenv()

# # Tạo lại cơ sở vector từ thư mục lưu trữ
# reviews_vector_db = Chroma(
#     persist_directory=REVIEWS_CHROMA_PATH,
#     embedding_function=OpenAIEmbeddings(),
# )

# # Thực hiện một truy vấn tìm kiếm thử nghiệm
# query = "What is Oriented Object Programming?"
# results = reviews_vector_db.similarity_search(query, k=6)

# # In ra kết quả
# for i, doc in enumerate(results):
#     print(f"Document {i + 1}:")
#     print(doc.page_content)
#     print("-" * 50)



from chatbot import review_chain

chat_history = []
# Suggested code may be subject to a license. Learn more: ~LicenseLog:973749580.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:2809998955.
question = """Đa hình là gì ?"""
# answer = review_chain.invoke(question)
result = review_chain.invoke({"question": question, "chat_history": chat_history})
print(result)
