from django.test import TestCase

# Create your tests here.
import redis

my_redis = redis.Redis(host='192.168.201.128', port=6379)
my_redis.keys('*')
print(my_redis)

