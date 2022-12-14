import datetime
import redis
import sys
from unittest.mock import Mock
import numpy as np
import cv2
import os

sys.path.append("../")
sys.path.append("../../camera")

from human_detection import Human_Detection_Worker


r = redis.Redis(host='localhost', port=6379)
r.flushdb()

def test_1():
    mock = Mock()

    hdw = Human_Detection_Worker(mock, mock, mock, mock, mock, mock)

    os.system("ls -la")
    test_file = open("test/test.jpeg", "rb")
    binary_data = test_file.read()

    # Get the original  byte array size
    size = sys.getsizeof(binary_data) - 33
    # Jpeg-encoded byte array into numpy array
    np_array = np.frombuffer(binary_data, dtype=np.uint8)
    np_array = np_array.reshape((size, 1))
    # Decode jpeg-encoded numpy array
    image = cv2.imdecode(np_array, 1)

    assert  hdw.detect_number_of_humans(image) == 2

def test_3():
    mock = Mock()
    #print("ola")
    #print(mock)

    hdw = Human_Detection_Worker(mock, mock, mock, mock, mock, mock)

    print(hdw.create_database_entry("camera_testing", 1, 1, str(datetime.datetime.now())))

    assert r.hget("camera_testing", 1) != None
    assert r.hget("camera_testing", 2) == None

def test_4():
    mock = Mock()
    #print("ola")
    #print(mock)

    hdw = Human_Detection_Worker(mock, mock, mock, mock, mock, mock)

    print(hdw.create_database_entry("camera_testing", 1, 1, str(datetime.datetime.now())))
    print(hdw.create_database_entry("camera_testing", 2, 1, str(datetime.datetime.now())))
    print(hdw.create_database_entry("camera_testing", 3, 1, str(datetime.datetime.now())))

    assert hdw.alarm_if_needed("camera_testing", 3) == True



    

    


    
    
    

   

    
    