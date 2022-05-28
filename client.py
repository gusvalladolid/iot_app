from http import client
from iiot_device import Sensor
import json
import time

#Creacion de un objeto de la clase HHTPConnetion
_conn = client.HTTPConnection('localhost', port=5000)

#Creacion de un objeto de la clase Sensor
s = Sensor()
h = {'Content-type': 'application/json'}  

while True:
    data = {
        'id': 1,
        'name': 'Temp Sensor',
        'value': s.get_random_number()
    }

    json_data = json.dumps(data)

    _conn.request('GET', '/devices', json_data, headers=h)
    _conn.close()


    value = data['value']
    if value >= 15:
        print(value ," -- Es mayor o igual 15")
        
    else:
        print(value ," -- No es mayor")

    time.sleep(1)