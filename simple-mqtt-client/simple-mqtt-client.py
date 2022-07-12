import paho.mqtt.client as mqtt 
import logging
import time
import json

logging.basicConfig(level=logging.INFO)

#docker internal mDNS service name
mqttBroker ="mqtt" 

client = mqtt.Client("Ping")
client.connect(mqttBroker) 
val = 0


while True:
    val = val + 1
    line=f"ping,tag1=tagval ping={val}"
    client.publish("PING", line)
    logging.info(f"Just published {val} to topic PING")
    time.sleep(1)