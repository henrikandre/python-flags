from pymemcache.client import base


client = base.Client(("127.0.0.1", 11211))  # Replace with your Memcached server address

key = 'feature_flag'
value = 'test'

# Set a value in Memcached
client.set(key, value)

# Retrieve a value from Memcached
result = client.get(key)

data_string = result.decode('utf-8')

print(f'Client 1 - Value from Memcached: {data_string}')
