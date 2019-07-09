import redis
import random
from pprint import pprint

# localhost="localhost" # linux, windows
localhost = "192.168.99.100"  # mac

random.seed(444)
hats = {
    f"hat:{random.getrandbits(32)}": i
    for i in (
        {
            "color": "black",
            "price": 49.99,
            "style": "fitted",
            "quantity": 1000,
            "npurchased": 0,
        },
        {
            "color": "maroon",
            "price": 59.99,
            "style": "hipster",
            "quantity": 500,
            "npurchased": 0,
        },
        {
            "color": "green",
            "price": 99.99,
            "style": "baseball",
            "quantity": 200,
            "npurchased": 0,
        },
    )
}

# show hats as json
pprint(hats)

# choosing db=1
# use 'SELECT 1' from the redis-cli
r = redis.Redis(host=localhost, port=6379, db=1)

# create a pipeline of transactions
# use hash multiset with h_id as key and several field-value pairs
with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute()

# Tell the Redis server to save its data to disk.
# Unlike save(), this method is asynchronous and returns immediately.
bgsave = r.bgsave()
print('r.bgsave()',bgsave)

print('r.hgetall("hat:56854717")')
pprint(r.hgetall("hat:56854717"))

print('r.keys()')
print(r.keys())

print('r.hincrby("hat:56854717", "quantity", -1)')
print(r.hincrby("hat:56854717", "quantity", -1))

print('r.hget("hat:56854717", "quantity")')
print(r.hget("hat:56854717", "quantity"))

print('r.hincrby("hat:56854717", "npurchased", 1)')
print(r.hincrby("hat:56854717", "npurchased", 1))