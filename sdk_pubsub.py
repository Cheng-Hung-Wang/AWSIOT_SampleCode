#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time

from mqtt_connect import sdk_connect

# If broker asks client ID.
client_id = ""

# topic configuration
topic = "test/topic" 

# qos configuration
qos = 1

def callback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

if __name__=='__main__':
    mqttc = sdk_connect(client_id)

    # check my_mqtt connectiong
    if not mqttc:
        exit(2)

    mqttc.subscribe(topic, qos, callback)

    while True:
        message = input("key in publish data:")
        
        if message=="exit":
            exit(0)
        # set topic, message, and qos=1
        mqttc.publish(topic, message, qos)
        time.sleep(1)
