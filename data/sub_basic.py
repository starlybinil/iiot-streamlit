import paho.mqtt.client as mqtt
import psycopg2 as pg
from datetime import datetime
import json

conn = pg.connect(host="localhost", dbname='postgres', user='postgres', password='p3800mhz')
try:
    cur = conn.cursor()
    print("Connection Established")
except (Exception, pg.DatabaseError) as error:
    print(error)


#MQTT Setup
#mqttBroker = 'broker.hivemq.com'
mqttBroker = 'test.mosquitto.org'

port = 1883
topic1 = 'Binil/Machine1/SensorData'


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc!=0:
        print("Connection not established. Something went wrong....")
   
    result = client.subscribe(topic1)

def on_disconnect(client, userdata,rc=0):
   
    client.loop_stop()

def on_log(client, userdata, level, buff): 
    print(buff)

def on_message(client, userdata, message):
    
    if message.topic == "Binil/Machine1/SensorData":
        msg = message.payload.decode("utf-8")
        dataObj=json.loads(msg)
        print("Machine 1")        

    machine_id = 200
    date = dataObj["sentDate"]
    timestamp = datetime.now()
    pressure = dataObj["Pressure"]
    humidity = dataObj["Humidity"]
    temperature = dataObj["Temperature"]
    status = dataObj['Status']

    insert_query = """ INSERT INTO machines ("id", "Timestamp", "sentDate", "Temperature", "Pressure", "Humidity", "status") VALUES (%s,%s,%s,%s,%s,%s, %s)"""
    record = (machine_id, timestamp, date, temperature, pressure, humidity, status)
    try:
        cur.execute(insert_query, record)
        print("DB transaction executed")

        #commit all transactions to the DB        
        conn.commit()
        print("DB transactions committed")

    except (Exception, pg.DatabaseError) as error:
        print(error)

client = mqtt.Client()
#subscribe to the hivemq broker
client.connect(mqttBroker, port, keepalive=60)

#call-back functions
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log
client.on_disconnect = on_disconnect

client.loop_forever()
