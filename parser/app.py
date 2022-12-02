import redis
red = redis.Redis(host='redis-12955.c52.us-east-1-4.ec2.cloud.redislabs.com',
                  port=12955,
                  password='6oQ1uygv5anY Z1EC2uAa3gnuCdVpQjoC')
red.set('var1', 'value1') # записываем в кеш строку "value1"
print(red.get('var1')) # считываем из кэша данные