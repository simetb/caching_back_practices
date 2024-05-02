import redis

# Conection to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Store data in cache
r.set('key', 'value')

# Get the data from cache
value = r.get('key')
print(value)