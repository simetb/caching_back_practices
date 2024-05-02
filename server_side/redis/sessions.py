import redis 

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Save the user session
r.hmset('session:user_id', {'name':'user_name','email':'user_email'})

# Get the user session
session_values = r.hgetall('session:user_id')
print(session_values)