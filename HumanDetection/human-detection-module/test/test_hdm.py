import redis

r = redis.Redis(host='localhost', port=6379)

def test_1():
    assert r.exists("Cameras")


def test_2():
    assert len(r.hgetall("Cameras")) > 0
   

    
    