"""Global helpers module."""
import redis


def get_redis_instance():
    return redis.StrictRedis(host='localhost',
                             port=1234,
                             db='0')
