import datetime
import redis
import sys
from unittest.mock import Mock

sys.path.append("../")
sys.path.append("../../camera")

from human_detection import Human_Detection_Worker


r = redis.Redis(host='localhost', port=6379)


#def test_1():
#    assert r.exists("camera_1")


#def test_2():
#    assert len(r.hgetall("camera_1")) > 0

def test_3():
    mock = Mock()
    #print("ola")
    #print(mock)

    hdw = Human_Detection_Worker(mock, mock, mock, mock)

    print(hdw.create_database_entry("camera_testing", 1, 1, str(datetime.datetime.now())))

    assert r.hget("camera_testing", 1) != None
    assert r.hget("camera_testing", 2) == None


    

    


    
    
    

   

    
    