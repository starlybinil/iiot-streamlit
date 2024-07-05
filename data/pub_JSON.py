import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
from datetime import datetime
import json

#MQTT Setup
port = 1883
#mqttBroker = 'broker.hivemq.com'
mqttBroker = 'test.mosquitto.org'
client = mqtt.Client()

def on_log(client, userdata, level, buffer):
    print("Log: ", buffer)

# Connect to the MQTT broker
client.connect(mqttBroker, port, 60)

client.on_log = on_log

#variables
dataObj={}
counter=0

while True:
    T = round(uniform(10.0, 50.0),2)  
    P = randrange(50, 100)
    H = randrange(10, 100)
    
    now = datetime.now()
   
    dataObj['machine_id'] = 200
    dataObj["sentDate"] = str(now)
    dataObj["Temperature"] = T
    dataObj["Pressure"] = P
    dataObj["Humidity"] = H
    dataObj["Status"] = "ON"

    jsondata = json.dumps(dataObj)
    client.publish("Binil/Machine1/SensorData", jsondata, qos=0)
    print("JSON data sent", dataObj)

    counter+=1
    if counter % 50 == 0:
        dataObj["sentDate"] = str(now)
        dataObj["Temperature"] = 0
        dataObj["Pressure"] = 0
        dataObj["Humidity"] = 0
        dataObj["Status"] = "OFF"
        client.publish("Binil/Machine1/SensorData", jsondata, qos=0)
        time.sleep(50)
    else:
        time.sleep(3)