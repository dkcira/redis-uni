import redis
import datetime

#localhost="localhost" # linux, windows
localhost="192.168.99.100" # mac

# Redis is the central class of the redis-py package. The TCP connect is done behind the scenes
# redis commands are called using the the class instance 'r'
r = redis.Redis(host=localhost,
                port=6379,
                db=0)

today = datetime.date.today()
visitors = {"dan", "jon", "alex"}
#r.sadd(today, *visitors) # this fails because the date is not a known input type

stoday = today.isoformat() # python 3.7+, or use str(today)
print(stoday, type(stoday))
r.sadd(stoday, *visitors)

# get members back
print('members', r.smembers(stoday))
# show cardinality of key
print('cardinality', r.scard(today.isoformat()))
