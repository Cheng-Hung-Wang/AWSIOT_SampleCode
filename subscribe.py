#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mqtt_connect import connect

# If broker asks client ID.
client_id = ""

# topic configuration
topic = "topicfilter/iotmonitor/provisioning/8050373158915119971"
#topic = "test/topic" 

# qos configuration
qos = 1

#called while client tries to establish connection with the server 
def on_connect(mqttc, userdata, flags, rc):
    if rc==0:
        print("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

#called when a topic is successfully subscribed to
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+ " data:"+str(obj))

#called when a message is received by a topic
def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

if __name__=='__main__':
    mqttc = connect(client_id)

    # check connection
    if not mqttc:
        exit(2)

    mqttc.on_connect = on_connect
    mqttc.on_subscribe = on_subscribe
    mqttc.on_message = on_message

    # subscirbe from topic publish
    mqttc.subscribe(topic, qos=qos)

    #automatically handles reconnecting
    mqttc.loop_forever()

