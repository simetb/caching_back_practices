import redis
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# Create a connection to the Redis server
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Example: Setting a key value pair
redis_client.set('my_key', 'my_value')

# Example: Getting the value for a key
value = redis_client.get('my_key')
print(value.decode('utf-8'))  # Decode the bytes to string if needed