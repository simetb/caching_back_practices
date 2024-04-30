from flask import Flask, jsonify, request, make_response
import base64

app = Flask(__name__)

# Example data
DATA = {
    'message': 'Hello World!, this is a resource'
}

def change_resource(new_massage):
    DATA['message'] = new_massage

# Route to get data
@app.route('/resource', methods=['GET'])
def get_resource():
    etag = generate_etag(DATA["message"])
    if_match = request.headers.get('If-None-Match') 
    if if_match == etag:
        return make_response('', 304, {'ETag': etag})
    else:
        response = jsonify(DATA)
        response.headers['ETag'] = etag
        response.headers['Cache-Control'] = 'max-age=3600'  
        return response
    
# Change the resource
@app.route('/resource', methods=['PUT'])
def put_resource():
    request_json = request.json
    
    if not request_json:
        return jsonify({'error': 'wrong body request JSON'}), 400
    
    message = request_json.get('new_message')
    
    change_resource(message)
    return f"El valor del mensaje es: {message}"

# Generate etag
def generate_etag(data):
    return base64.b64encode(data.encode('utf-8')).decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)