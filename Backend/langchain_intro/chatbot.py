import dotenv #  nhập thư viện dotenv để tải biến môi trường
from langchain_openai import ChatOpenAI # nhập thư viện ChatOpenAI từ langchain_openai
from langchain.prompts import ( # nhập các lớp PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate từ langchain.prompts
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain_core.output_parsers import StrOutputParser # nhập lớp StrOutputParser từ langchain_core.output_parsers
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough

REVIEWS_CHROMA_PATH = "chroma_data/"

dotenv.load_dotenv() # tải biến môi trường


#TEMPLATE
review_template_str = """Your job is to use the knowledge of object-oriented programming that I provide to answer questions about this subject for the students. Use the following context to answer the question. Be as detailed as possible, but don't make up any information that isn't in context. If you don't know the answer, you can search that question on Google. If you can't find the answer, just say you don't know

{context}
"""

# Tạo prompt cho hệ thống
review_system_prompt = SystemMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["context"],
        template=review_template_str,
    )
)

# Tạo prompt cho người dùng
review_human_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        input_variables=["question"],
        template="{question}",
    )
)

# Danh sách các prompt
messages = [review_system_prompt, review_human_prompt]

# Tạo prompt template cho chat
review_prompt_template = ChatPromptTemplate(
    input_variables=["context", "question"],
    messages=messages,
)

reviews_vector_db = Chroma(
    persist_directory=REVIEWS_CHROMA_PATH,
    embedding_function=OpenAIEmbeddings()
)

reviews_retriever  = reviews_vector_db.as_retriever(k=10)

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

# review_chain = review_prompt_template | chat_model

output_parser = StrOutputParser() #2
review_chain = (
    {"context": reviews_retriever, "question": RunnablePassthrough()}
    | review_prompt_template
    | chat_model
    | StrOutputParser()
)

# mẫu để chạy
# >>> from langchain_intro.chatbot import review_chain

# >>> context = "I had a great stay!"
# >>> question = "Did anyone have a positive experience?"

# >>> review_chain.invoke({"context": context, "question": question})
# AIMessage(content='Yes, the patient had a great stay and had a
# positive experience at the hospital.')