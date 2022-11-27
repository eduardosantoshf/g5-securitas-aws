import redis

try:
    r = redis.Redis(
                host='human-detection-cache.gxdzdr.ng.0001.euw3.cache.amazonaws.com',
                #host = 'localhost',
                port=6379,
                ssl=True,
                ssl_cert_reqs=None
            )
    print(r)

    try:
        print(r.ping())
        print(r.set('foo','bar'))
        r.get('foo')
    except Exception as e:
        print('get set error: ', e)

except Exception as e:
    print('redis err: ', e)