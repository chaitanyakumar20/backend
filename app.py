from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return "Welcome to the API. Use /bfhl for POST and GET requests.", 200

# POST Method - /bfhl
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    data = request.get_json().get("data", [])

    full_name = "john_doe"
    dob = "17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    user_id = f"{full_name}_{dob}"

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }

    return jsonify(response), 200

# GET Method - /bfhl
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({
        "operation_code": 1
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
