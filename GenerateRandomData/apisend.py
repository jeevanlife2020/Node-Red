import paho.mqtt.client as mqtt
import time
import json
import random

config_data={
    "total_usage":0,
    "flow_rate":0
}

mqtt_pub_topic="iot-2/evt/status/fmt/json"
client=mqtt.Client(client_id="d:tzu8pr:SWMS:2920")

def on_connect(client, userdata, flags, rc):
    client.connected_flag=True
    client.disconnect_flag=False
    print("Connected")
    print("rc: " + str(rc))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))
    client.connected_flag=False
    client.disconnect_flag=True
    client.loop_stop()

def on_message(client, userdata, message):
    message_received=json.loads(message.payload)
    print("message received  ",message_received)

def init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password):
    mqtt.Client.connected_flag=False
    client.username_pw_set(username=mqtt_uid,password=mqtt_password)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect    
    client.on_publish = on_publish
    client.connect(mqtt_host, int(mqtt_port))
    #client.subscribe(mqtt_topic)
    client.loop_start()
    while not client.connected_flag: #wait in loop
        print("In wait loop")
        time.sleep(1)
    #return 0

def handler():
    mqtt_host="tzu8pr.messaging.internetofthings.ibmcloud.com"
    mqtt_port="1883"
    mqtt_uid="use-token-auth"
    mqtt_password="Proteem@290695"
    #Connection initiated
    init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password)
    usage_data=0
    while True:
        if(client.connected_flag):
            usage_data=usage_data+generateRandomData(1,10)
            flow_data=generateRandomData(0,100)
            config_data["total_usage"]=usage_data
            config_data["flow_rate"]=flow_data
            client.publish(str(mqtt_pub_topic),str(config_data))
            print(config_data)
            time.sleep(1)
        else:
            client.loop_stop()
            init_mqtt(client,mqtt_host,mqtt_port,mqtt_uid,mqtt_password)
            time.sleep(5)

def generateRandomData(min,max):
    value=random.randint(min,max)
    return value


if __name__ == "__main__": 
    handler()