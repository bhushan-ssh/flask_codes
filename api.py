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
    data= {"Hey there!": "Welcome to the API"}

    return jsonify(data),404
    



@app.route('/api/addition/<int:num1>/<int:num2>', methods=['GET'])
def addition(num1, num2):
    result = num1 + num2
    return jsonify({'result': result})


@app.route('/api/addition_req', methods=['GET'])
def addition_req():
    req_data = request.get_json()
    print(req_data)
    # return jsonify(req_data)
    return jsonify("recieved data successfully"),200


if __name__ == '__main__':
    app.run(debug=True) 

