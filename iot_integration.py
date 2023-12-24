```python
# Import necessary libraries
import pandas as pd
import time
from paho.mqtt import client as mqtt_client

# Define the broker and topic for the IoT device
broker = 'mqtt.eclipse.org'
port = 1883
topic = "EnvironmentalData"

# Function to connect to the MQTT broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Function to subscribe to the topic
def subscribe(client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

# Function to collect data from the IoT device
def collect_data(client):
    client.loop_start()
    time.sleep(10)
    client.loop_stop()

# Connect to the MQTT broker
client = connect_mqtt()

# Subscribe to the topic
subscribe(client)

# Collect data from the IoT device
collect_data(client)

# Note: This is a basic example of how to collect data from an IoT device using MQTT.
# In a real-world scenario, you would need to parse the received data and store it in a suitable format for further processing.
# You might also need to handle multiple IoT devices and topics.
```
