import redis

# Estabelecer conexão com o servidor Redis local
r = redis.Redis(host='localhost', port=6379, db=0)
