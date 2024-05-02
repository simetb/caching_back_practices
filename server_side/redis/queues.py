import redis

# Connection to redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Publish a message to the channel
r.lpush('chanel', 'First message')
r.lpush('chanel', 'Second message')
r.lpush('chanel', 'Third message')
r.lpush('chanel', 'Fourth message')

# Subscribe to the channel
pubsub = r.pubsub()
pubsub.subscribe('chanel')

# Listen to the channel
for message in pubsub.listen():
    print(message)