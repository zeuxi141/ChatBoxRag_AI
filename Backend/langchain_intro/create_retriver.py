# Import các thư viện cần thiết
import dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Đường dẫn đến file CSV chứa dữ liệu đánh giá
REVIEWS_CSV_PATH = "data/reviews.csv"
# Đường dẫn đến thư mục lưu trữ cơ sở vector
REVIEWS_CHROMA_PATH = "chroma_data"

# Load biến môi trường từ file .env
dotenv.load_dotenv()

# Tạo đối tượng CSVLoader để đọc dữ liệu từ file CSV
loader = CSVLoader(file_path=REVIEWS_CSV_PATH, source_column="Review")
# Load dữ liệu đánh giá từ file CSV
reviews = loader.load()

# Xử lý metadata (nếu có)
for doc in reviews:
    # Nếu metadata là None, thay thế bằng dictionary rỗng
    if doc.metadata is None:
        doc.metadata = {}
    else:
        # Chuyển metadata thành chuỗi nếu cần thiết
        doc.metadata = {k: str(v) if v is not None else "" for k, v in doc.metadata.items()}

# Tạo cơ sở vector từ dữ liệu đánh giá
reviews_vector_db = Chroma.from_documents(
    reviews, OpenAIEmbeddings(), persist_directory=REVIEWS_CHROMA_PATH
)


# Thông báo khi quá trình hoàn thành
print("Vector database đã được tạo và lưu trữ thành công !")
