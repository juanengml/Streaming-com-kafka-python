from kafka import KafkaConsumer
from json import loads
import json
import cv2
import numpy as np
import sys 
#from lgetter.Model.v1.pose import Estimation
#from lgether.comm import Producer

consumer = KafkaConsumer('productions-v1',
                        bootstrap_servers = ['localhost:29092'])

for message in consumer:
    body = message.value
    #print(body)
    size = sys.getsizeof(body)
    np_array = np.frombuffer(body, dtype=np.uint8)
    #print(size,np_array)
    image = cv2.imdecode(np_array, 1)
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print(img) 
    #result = Estimation.start(img)
    #producer_send = Producer.send(result)
