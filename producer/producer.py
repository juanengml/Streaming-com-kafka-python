kfrom kafka import KafkaProducer
import time
import json
from datetime import datetime
#import base64
import cv2


producer = KafkaProducer(bootstrap_servers = ['localhost:29092'])
#producer.send('productions-v1', b'Hello kafka')

capture = cv2.VideoCapture("mp4/shark.mp4")

#encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

counter = 0 
inicio = datetime.now()

while True:
    
    ret, frame = capture.read()
    if ret is True:
      result, imencode = cv2.imencode('.jpg', frame, encode_param)
      #print(type(imencode.tobytes()))
      producer.send('productions-v1', imencode.tobytes())
      counter = counter + 1
      print("FRAME NUMERO: %s.mp4" % counter)
     #print(len(imgencode.tobytes()))
     #producer.publish(imgencode.tobytes(), content_type='image/jpeg', content_encoding='binary')
    time.sleep(0.001)

capture.release()
fim = datetime.now()

print("TEMPO DE RESPOSTA: ", fim - inicio)
