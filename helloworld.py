"""Simple script to test connection to Redis and print an existing key."""
from redis import StrictRedis
import os

#localhost="localhost" # linux
localhost="192.168.99.100" # mac

redis = StrictRedis(host=os.environ.get("REDIS_HOST", localhost),
                    port=os.environ.get("REDIS_PORT", 6379),
                    db=0)

print(redis.get("hello"))
