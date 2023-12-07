from pymemcache.client import base

client = base.Client(("10.196.38.52", 11211))  # Memcached server address

key = 'feature_flag'
value = 'flag1'

# change value to flag2 for second feature flag

# Set a value in Memcached
client.set(key, value)

# Retrieve a value from Memcached
result = client.get(key)

data_string = result.decode('utf-8')

print(f'Client 1 - Value from Memcached: {data_string}')
