from redis import Redis
def get_redis_connection(option):
    return Redis(host=option.get("host"), port=option.get("port"), db=option.get("db"))