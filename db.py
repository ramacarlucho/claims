import os

import redis

REDIS_HOST = os.getenv('REDIS_HOST', None)
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
if REDIS_HOST:
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
    )
else:
    r = redis.Redis()


def get_claimable(addr:str):
    return r.get(addr)

def set_claimable(addr:str, claim:float):
    r.mset({addr: claim})
    return None, None