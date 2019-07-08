import redis

#localhost="localhost" # linux, windows
localhost="192.168.99.100" # mac

# Redis is the central class of the redis-py package. The TCP connect is done behind the scenes
# redis commands are called using the the class instance 'r'
r = redis.Redis(host=localhost,
                port=6379,
                db=0)

r.mset({'Croatia': 'Zagreb', 'Bahamas': 'Nassau'})
# bytes type
print(r.get('Bahamas'))
# string type
print(r.get('Bahamas').decode('utf-8'))
