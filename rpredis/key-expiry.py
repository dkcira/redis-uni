import redis
from datetime import timedelta
import time

# localhost="localhost" # linux, windows
localhost = "192.168.99.100"  # mac

# choosing db=1
# use 'SELECT 1' from the redis-cli
r = redis.Redis(host=localhost, port=6379, db=1)

# setex: 'SET' with expiration
r.setex(
    "runner",
    timedelta(minutes=1),
    value="now you see me, now you don't"
)

print('time to livein seconds')
print(r.ttl('runner'))

print('time to live in milliseconds')
print(r.pttl("runner"))

print(r.get("runner"))

r.expire("runner", timedelta(seconds=3)) # set new expiration window

# sleep 4 seconds
time.sleep(4)
print(r.get("runner"))
print(r.exists("runner")) # key & value are both expired