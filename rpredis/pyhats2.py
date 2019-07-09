import logging
import redis
import random
from pprint import pprint

# logging (part of standard library)
logging.basicConfig()

# localhost="localhost" # linux, windows
localhost = "192.168.99.100"  # mac

# choosing db=1
# use 'SELECT 1' from the redis-cli
r = redis.Redis(host=localhost, port=6379, db=1)


class OutOfStockError(Exception):
    """Raised when PyHats.com is all out of today's hottest hat"""

def buyitem(r: redis.Redis, itemid: int) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # optimistic locking
                # Get available inventory, watching for changes
                # related to this itemid before the transaction
                pipe.watch(itemid)
                nleft: bytes = r.hget(itemid, "quantity")
                if nleft > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Stop watching the itemid and raise to break out
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Log total num. of errors by this user to buy this item,
                # then try the same process again of WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None

if __name__ == '__main__':
    buyitem(r, "hat:56854717")
    buyitem(r, "hat:56854717")
    buyitem(r, "hat:56854717")
    print(r.hmget("hat:56854717", "quantity", "npurchased"))

    #  buy remaining 196 hats and deplete stock to 0
    for _ in range(196):
        buyitem(r, "hat:56854717")
    print(r.hmget("hat:56854717", "quantity", "npurchased"))