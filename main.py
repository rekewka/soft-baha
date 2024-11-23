from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Parse incoming JSON request
        data = request.json
        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation', 'add')  # Default to addition

        if num1 is None or num2 is None:
            return jsonify({"error": "Please provide both num1 and num2"}), 400

        # Perform calculation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({"error": "Division by zero is not allowed"}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
