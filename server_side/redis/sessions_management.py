import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Save the game state
r.hset('game:state', 'playing', 'ubication')

# Obtaine the game state
print(r.hget('game:state', 'playing'))