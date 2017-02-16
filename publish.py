#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mqtt_connect import connect

# If broker asks client ID.
client_id = ""

# topic configuration
topic = "topicfilter/iotmonitor/provisioning/8050373158915119971"

# qos configuration
qos = 1

if __name__=='__main__':
    mqttc = connect(client_id)

    # check connection
    if not mqttc:
        exit(2)

    while True:
        message = input("key in publish data:")
        
        if message=="exit":
            exit(0)

        # set topic, message, and qos=1
        mqttc.publish(topic, message, qos)
