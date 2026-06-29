from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'id': 1,
        'name': 'Sample Data',
        'description': 'This is a sample data response from the API.'
    }
    return jsonify(sample_data)


@app.route('/api/hello', methods=['GET'])
def hello():
    data = {"Hey there!": "Welcome to the API"}
    return jsonify(data), 200

@app.route('/api/addition/<int:num1>/<int:num2>', methods=['GET'])
def addition(num1, num2):
    result = num1 + num2
    return jsonify({'result': result})

@app.route('/user/<string:name>')
def user(name):
    return jsonify({
        "username": name,
        "status": "active"
    })

@app.route('/api/subtract/<int:num1>/<int:num2>', methods=['GET'])
def subtract(num1, num2):
    result = num1 - num2
    return jsonify({'result': result})

@app.route('/api/multiply/<int:num1>/<int:num2>', methods=['GET'])
def multiply(num1, num2):
    result = num1 * num2
    return jsonify({'result': result})

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({'echo': data}), 200

@app.route('/api/addition_req', methods=['GET'])
def addition_req():
    req_data = request.get_json()
    print(req_data)
    # return jsonify(req_data)
    return jsonify("recieved data successfully"),200

@app.route('/api/divide/<int:num1>/<int:num2>', methods=['GET'])
def divide(num1, num2):
    if num2 == 0:
        return jsonify({'error': 'Division by zero'}), 400
    result = num1 / num2
    return jsonify({'result': result})

@app.route('/api/modulo/<int:num1>/<int:num2>', methods=['GET'])
def modulo(num1, num2):
    if num2 == 0:
        return jsonify({'error': 'Division by zero'}), 400
    result = num1 % num2
    return jsonify({'result': result})

@app.route('/api/power/<int:base>/<int:exponent>', methods=['GET'])
def power(base, exponent):
    result = base ** exponent
    return jsonify({'result': result})

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')
    num2 = data.get('num2')
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Unknown operation'}), 400
    
    return jsonify({'result': result}), 200


if __name__ == '__main__':
    app.run(debug=True) 

