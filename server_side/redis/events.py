import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Increment counter
r.incr('counter')

# Get counter
print(r.get('counter'))