from flask import Flask, jsonify, request
from flask_cors import CORS
from chatbot import review_chain

# Lưu trữ lịch sử chat
chat_history = [("question1", "answer1"), ("question2", "answer2")]

# Khởi tạo Flask app
app = Flask(__name__)
# Cho phép CORS từ localhost:3000
cors = CORS(app, origins=['http://localhost:3000'])


@app.route('/api/chat', methods=['POST'])
def api():
    # Kiểm tra phương thức yêu cầu
    if request.method == 'POST':
        try:
            # Lấy dữ liệu từ yêu cầu
            data = request.get_json()
            # Lấy câu hỏi từ dữ liệu
            query = data.get('message')
            print("query: " +  query)
            
            # Gọi hàm review_chain để xử lý câu hỏi
            result = review_chain.invoke(query)
            print(f"Result type: {type(result)}, Result: {result}")
            
            # Kiểm tra kiểu dữ liệu của result và xử lý
            if isinstance(result, dict) and "answer" in result:
                answer = result["answer"]
            else:
                answer = result  # Nếu result là một chuỗi
            
            # Lưu trữ lịch sử chat
            chat_history.append((query, answer))
            # Trả về kết quả
            return jsonify({'message': answer})
        
        # Xử lý lỗi
        except Exception as e:
            print(f"Error processing request: {e}")
            return jsonify({'error': 'Error processing request'}), 500

# Chạy server
if __name__ == '__main__':
    app.run(port=5000)
