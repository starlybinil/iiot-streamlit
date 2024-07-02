import paho.mqtt.client as mqtt

#MQTT Setup
mqttBroker = 'broker.hivemq.com'
port = 1883
topic1 = 'binil/machine1/Temperature'
topic2 = 'binil/machine1/Status'
topic3 = 'binil/machine1/Pressure'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc!=0:
        print("Connection not established. Something went wrong....")
   
    client.subscribe(topic1)
    client.subscribe(topic2)
    client.subscribe(topic3)

def on_message(client, userdata, msg):
    if msg.topic == topic1:
        print(f"Temperature: {msg.payload.decode()} C")
    if msg.topic == topic2:
        print(f"Machine Status: {msg.payload.decode()} C")
    if msg.topic == topic3:
        print(f"Pressure: {msg.payload.decode()} C")


client = mqtt.Client()

#call-back functions
client.on_connect = on_connect
client.on_message = on_message

#subscribe to the hivemq broker
client.connect(mqttBroker, port, keepalive=60)

client.loop_forever()