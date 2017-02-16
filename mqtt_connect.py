#!/usr/bin/env python3
#-*- coding: utf-8 -*-



# host is your endpoing and mqtt port number
host = "your end point"
port = 8883


# root cert file path
root_CA = "cert/root-CA.crt"

# cerfiticate file path
cert_file = "cert/certificate.pem.crt"

# private key file path
key_file = "cert/private.pem.key"


def check_fail():
    missing = False

    if not host:
        print("Missing endpoint'")
        missing = True

    if not root_CA:
        print("Missing rootCA")
        missing = True

    if not cert_file:
        print("Missing cert file")
        missing = True

    if not key_file:
        print("Missing private key")
        missing = True
    return missing

# use paho mqtt connect to aws mqtt brocker
def connect(client_id):
    import ssl
    import paho.mqtt.client as mqtt

    if check_fail():
        return False

    #creating a client 
    mqttc = mqtt.Client(client_id=client_id)


    #Configure network encryption and authentication options. Enables SSL/TLS support.
    #adding client-side certificates and enabling tlsv1.2 support as required by aws-iot service
    mqttc.tls_set(root_CA, certfile=cert_file, keyfile=key_file, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

    #connecting to aws-account-specific-iot-endpoint
    #AWS IoT service hostname and portno
    mqttc.connect(host, port=port)
    return mqttc


# use aws python sdk connect to aws mqtt broker
def sdk_connect(client_id):
    import logging
    from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

    # Configure logging
    logger = logging.getLogger("AWSIoTPythonSDK.core")
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)

    if check_fail():
        return False

    mqttc = AWSIoTMQTTClient(client_id)
    mqttc.configureEndpoint(host, port)
    mqttc.configureCredentials(root_CA, key_file, cert_file)

    # AWSIoTMQTTClient connection configuration
    mqttc.configureAutoReconnectBackoffTime(1, 32, 20)
    mqttc.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    mqttc.configureDrainingFrequency(2)  # Draining: 2 Hz
    mqttc.configureConnectDisconnectTimeout(10)  # 10 sec
    mqttc.configureMQTTOperationTimeout(5)  # 5 sec

    # Connect and subscribe to AWS IoT
    mqttc.connect()
    return mqttc

